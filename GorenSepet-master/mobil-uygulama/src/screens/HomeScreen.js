import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView, SafeAreaView } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { colors, spacing, typography, shadows, layout } from '../theme/theme';
import VoiceService from '../services/VoiceService';
import BeaconService from '../services/BeaconService';
import ApiService from '../services/ApiService';
import { supabase } from '../services/supabase';
import * as Location from 'expo-location';
import { useState, useEffect } from 'react';

export default function HomeScreen({ navigation }) {
    const [isListening, setIsListening] = useState(false);
    const [recognizedText, setRecognizedText] = useState('');
    const [isStaffNearby, setIsStaffNearby] = useState(false);
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Kullanıcı bilgisini çek
        const fetchUser = async () => {
            const { data: { user } } = await supabase.auth.getUser();
            setUser(user);
        };
        fetchUser();
        // Beacon taramasını başlat
        const initBeacon = async () => {
            await BeaconService.startScanning((beacon) => {
                console.log('Personnel station found nearby!', beacon);
                if (!isStaffNearby) {
                    setIsStaffNearby(true);
                    VoiceService.speak('Yakınınızda bir personel standı tespit edildi. Yardım isterseniz butona basabilir veya yardım diye seslenebilirsiniz.');
                }
            });
        };

        initBeacon();

        return () => {
            VoiceService.destroy();
            BeaconService.stopScanning();
        };
    }, []);

    const handleHelpRequest = async () => {
        VoiceService.speak('Konumunuz belirleniyor, lütfen bekleyin.');
        try {
            let { status } = await Location.requestForegroundPermissionsAsync();
            if (status !== 'granted') {
                VoiceService.speak('Konum izni reddedildi. Personel çağrılamıyor.');
                return;
            }

            let location = await Location.getCurrentPositionAsync({});
            
            if (user) {
                const { error } = await supabase.from('help_requests').insert({
                    user_id: user.id,
                    latitude: location.coords.latitude,
                    longitude: location.coords.longitude,
                    status: 'pending'
                });
                
                if (error) {
                    console.error('Supabase Help Request Error:', error);
                    throw error;
                }
                VoiceService.speak('Personel başarıyla çağrıldı, konumuz iletildi. Lütfen bekleyin.');
            } else {
                VoiceService.speak('Yardım çağırmak için giriş yapmalısınız.');
            }
        } catch (error) {
            console.error('Help Request Error:', error);
            VoiceService.speak('Çağrı sırasında bir bağlantı hatası oluştu.');
        }
    };

    const handleVoiceCommand = async (results) => {
        const text = results[0];
        setRecognizedText(text);
        const command = VoiceService.parseCommand(results);

        if (command === 'HELP') {
            await handleHelpRequest();
        } else if (command === 'SHOPPING') {
            VoiceService.speak('Alışverişe başlanıyor, kamera açılıyor.');
            console.log('Alışverişe Başla');
        } else if (command === 'SETTINGS') {
            VoiceService.speak('Ayarlar açılıyor.');
            console.log('Ayarlar');
        } else if (command === 'PROFILE') {
            VoiceService.speak('Profil ayarları açılıyor.');
            console.log('Profilim');
        } else {
            VoiceService.speak('Söylediğinizi arıyorum, lütfen bekleyin.');
            console.log('API ye yollaniyor:', text);
            const aiResponse = await ApiService.parseRecipe(text);
            
            if (aiResponse.basarili && aiResponse.malzemeler && aiResponse.malzemeler.length > 0) {
                const malzemeIsimleri = aiResponse.malzemeler.map(m => m.isim).join(', ');
                VoiceService.speak(`${aiResponse.yemek} için gerekli malzemeler alışveriş listenize eklenecektir: ${malzemeIsimleri}`);
            } else {
                VoiceService.speak(aiResponse.mesaj || 'Üzgünüm, bu komutu tam olarak anlayamadım.');
            }
        }

        setIsListening(false);
    };

    const toggleListening = async () => {
        if (isListening) {
            await VoiceService.stopListening();
            setIsListening(false);
        } else {
            setRecognizedText('');
            setIsListening(true);
            VoiceService.speak('Dinliyorum, buyurun.');
            await VoiceService.startListening(
                (results) => handleVoiceCommand(results),
                (error) => {
                    console.error(error);
                    setIsListening(false);
                }
            );
        }
    };

    const features = [
        {
            id: 1,
            title: 'Alışverişe Başla',
            icon: 'camera',
            color: colors.primary,
            onPress: () => {
                VoiceService.speak('Alışverişe başla seçildi.');
                console.log('Alışverişe Başla');
            },
            accessibilityHint: 'Kamerayı açar ve ürün taramaya başlar',
        },
        {
            id: 2,
            title: isListening ? 'Dinleniyor...' : 'Sesli Asistan',
            icon: isListening ? 'microphone-settings' : 'microphone',
            color: isListening ? colors.error : colors.secondary,
            onPress: toggleListening,
            accessibilityHint: 'Sesli komut sistemini başlatır',
        },
        {
            id: 3,
            title: isStaffNearby ? 'Görevli Yakında!' : 'Yardım Çağır',
            icon: isStaffNearby ? 'account-search' : 'bell-ring',
            color: isStaffNearby ? colors.success : colors.warning,
            onPress: handleHelpRequest,
            accessibilityHint: 'Konumunuzu paylaşarak mağaza personelinden fiziksel yardım ister',
        },
        {
            id: 4,
            title: 'Ayarlar',
            icon: 'cog',
            color: colors.textLight,
            onPress: () => {
                VoiceService.speak('Ayarlar açıldı.');
                console.log('Ayarlar');
            },
            accessibilityHint: 'Uygulama ayarlarını açar',
        },
    ];

    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.header}>
                <View>
                    <Text style={styles.greeting}>Merhaba,</Text>
                    <Text style={styles.username}>{user ? (user.email.split('@')[0]) : 'Misafir'}</Text>
                </View>
                <TouchableOpacity
                    style={styles.profileButton}
                    accessibilityLabel="Çıkış Yap"
                    accessibilityHint="Hesabınızdan güvenle çıkış yapar"
                    onPress={async () => {
                        await supabase.auth.signOut();
                        navigation.replace('Login');
                    }}
                >
                    <MaterialCommunityIcons name="logout" size={32} color={colors.primary} />
                </TouchableOpacity>
            </View>

            <ScrollView
                contentContainerStyle={styles.content}
                showsVerticalScrollIndicator={false}
            >
                <Text style={styles.sectionTitle}>Ne yapmak istersiniz?</Text>

                {recognizedText ? (
                    <View style={styles.feedbackContainer}>
                        <Text style={styles.feedbackLabel}>Duyduğum:</Text>
                        <Text style={styles.feedbackText}>"{recognizedText}"</Text>
                    </View>
                ) : null}

                <View style={styles.grid}>
                    {features.map((item) => (
                        <TouchableOpacity
                            key={item.id}
                            style={[styles.card, { borderLeftColor: item.color }]}
                            onPress={item.onPress}
                            activeOpacity={0.7}
                            accessibilityRole="button"
                            accessibilityLabel={item.title}
                            accessibilityHint={item.accessibilityHint}
                        >
                            <View style={[styles.iconContainer, { backgroundColor: item.color + '20' }]}>
                                <MaterialCommunityIcons name={item.icon} size={32} color={item.color} />
                            </View>
                            <Text style={styles.cardText}>{item.title}</Text>
                        </TouchableOpacity>
                    ))}
                </View>
            </ScrollView>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: colors.background,
    },
    header: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        paddingHorizontal: spacing.large,
        paddingTop: spacing.large,
        paddingBottom: spacing.medium,
        backgroundColor: colors.surface,
        ...shadows.small,
        marginBottom: spacing.medium,
    },
    greeting: {
        ...typography.body,
        fontSize: 16,
        color: colors.textLight,
    },
    username: {
        ...typography.header,
        fontSize: 24,
        color: colors.primaryDark,
    },
    sectionTitle: {
        ...typography.subheader,
        marginHorizontal: spacing.large,
        marginBottom: spacing.medium,
        color: colors.text,
    },
    content: {
        paddingBottom: spacing.xlarge,
    },
    grid: {
        paddingHorizontal: spacing.large,
        gap: spacing.medium,
    },
    card: {
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: colors.surface,
        padding: spacing.medium,
        borderRadius: layout.borderRadius,
        borderLeftWidth: 6,
        ...shadows.medium,
        minHeight: 100,
    },
    iconContainer: {
        width: 60,
        height: 60,
        borderRadius: 30,
        justifyContent: 'center',
        alignItems: 'center',
        marginRight: spacing.medium,
    },
    cardText: {
        ...typography.subheader,
        fontSize: 20,
        color: colors.text,
        flex: 1,
    },
    feedbackContainer: {
        marginHorizontal: spacing.large,
        marginBottom: spacing.medium,
        padding: spacing.medium,
        backgroundColor: colors.surface,
        borderRadius: layout.borderRadius,
        borderWidth: 1,
        borderColor: colors.divider,
        ...shadows.small,
    },
    feedbackLabel: {
        ...typography.body,
        fontSize: 12,
        color: colors.textLight,
        marginBottom: 4,
    },
    feedbackText: {
        ...typography.subheader,
        fontSize: 18,
        color: colors.primary,
        fontStyle: 'italic',
    },
});
