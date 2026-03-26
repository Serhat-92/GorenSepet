import { DeviceEventEmitter, Platform } from 'react-native';
import Beacons from 'react-native-beacons-manager';
import * as Location from 'expo-location';

class BeaconService {
    constructor() {
        this.beaconsDidRangeEvent = null;
        this.onBeaconFound = null;
        this.isScanning = false;

        // Örnek bir Staff Station Beacon UUID
        this.STAFF_STATION_UUID = 'F7826DA6-4FA2-4E98-8024-BC5B71E0893E';
        this.region = {
            identifier: 'StaffStation',
            uuid: this.STAFF_STATION_UUID
        };
    }

    async requestPermissions() {
        if (Platform.OS === 'ios') {
            Beacons.requestAlwaysAuthorization();
        }

        const { status } = await Location.requestForegroundPermissionsAsync();
        return status === 'granted';
    }

    async startScanning(onBeaconFound) {
        if (this.isScanning) return;

        this.onBeaconFound = onBeaconFound;

        try {
            const hasPermission = await this.requestPermissions();
            if (!hasPermission) {
                console.error('Location permission not granted for Beacon scanning');
                return;
            }

            // Beacon taramasını başlat
            if (Platform.OS === 'android') {
                Beacons.detectIBeacons();
                await Beacons.startRangingBeaconsInRegion('REGION1', this.STAFF_STATION_UUID);
            } else {
                await Beacons.startRangingBeaconsInRegion(this.region);
            }

            this.beaconsDidRangeEvent = Beacons.BeaconsEventEmitter.addListener(
                'beaconsDidRange',
                (data) => {
                    if (data.beacons && data.beacons.length > 0) {
                        // En yakın beacon'ı bul
                        const nearestBeacon = data.beacons.reduce((prev, curr) =>
                            (prev.distance < curr.distance) ? prev : curr
                        );

                        // Eğer beacon yeterince yakınsa (örn: 5 metre)
                        if (nearestBeacon.distance < 5) {
                            if (this.onBeaconFound) {
                                this.onBeaconFound(nearestBeacon);
                            }
                        }
                    }
                }
            );

            this.isScanning = true;
            console.log('Beacon scanning started');
        } catch (error) {
            console.error('Beacon scanning error:', error);
        }
    }

    async stopScanning() {
        if (!this.isScanning) return;

        try {
            if (Platform.OS === 'android') {
                await Beacons.stopRangingBeaconsInRegion('REGION1', this.STAFF_STATION_UUID);
            } else {
                await Beacons.stopRangingBeaconsInRegion(this.region);
            }

            if (this.beaconsDidRangeEvent) {
                this.beaconsDidRangeEvent.remove();
            }

            this.isScanning = false;
            console.log('Beacon scanning stopped');
        } catch (error) {
            console.error('Beacon stopping error:', error);
        }
    }
}

export default new BeaconService();
