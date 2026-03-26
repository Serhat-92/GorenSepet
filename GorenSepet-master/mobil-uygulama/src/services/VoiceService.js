import * as Speech from 'expo-speech';
import Voice from '@react-native-voice/voice';

class VoiceService {
    constructor() {
        this.isListening = false;
        this.onSpeechResults = null;
        this.onSpeechError = null;

        Voice.onSpeechStart = this._onSpeechStart.bind(this);
        Voice.onSpeechEnd = this._onSpeechEnd.bind(this);
        Voice.onSpeechResults = this._onSpeechResults.bind(this);
        Voice.onSpeechError = this._onSpeechError.bind(this);
    }

    // --- Text-to-Speech (Metin Okuma) ---
    async speak(text) {
        try {
            const isSpeaking = await Speech.isSpeakingAsync();
            if (isSpeaking) {
                await Speech.stop();
            }
            Speech.speak(text, {
                language: 'tr-TR',
                pitch: 1.0,
                rate: 1.0,
            });
        } catch (error) {
            console.error('Speech error:', error);
        }
    }

    async stopSpeaking() {
        await Speech.stop();
    }

    // --- Speech-to-Text (Sesli Komut) ---
    async startListening(onResults, onError) {
        if (this.isListening) return;

        this.onSpeechResults = onResults;
        this.onSpeechError = onError;

        try {
            await Voice.start('tr-TR');
            this.isListening = true;
        } catch (error) {
            console.error('Voice start error:', error);
            if (onError) onError(error);
        }
    }

    async stopListening() {
        if (!this.isListening) return;

        try {
            await Voice.stop();
            this.isListening = false;
        } catch (error) {
            console.error('Voice stop error:', error);
        }
    }

    async destroy() {
        try {
            await Voice.destroy();
            Voice.removeAllListeners();
        } catch (error) {
            console.error('Voice destroy error:', error);
        }
    }

    _onSpeechStart() {
        this.isListening = true;
        console.log('Speech started');
    }

    _onSpeechEnd() {
        this.isListening = false;
        console.log('Speech ended');
    }

    _onSpeechResults(event) {
        if (this.onSpeechResults && event.value) {
            this.onSpeechResults(event.value);
        }
    }

    _onSpeechError(event) {
        this.isListening = false;
        console.error('Speech error event:', event.error);
        if (this.onSpeechError) {
            this.onSpeechError(event.error);
        }
    }

    // --- Komut Çözümleme (Command Parsing) ---
    parseCommand(results) {
        const text = results[0].toLowerCase();
        
        if (text.includes('yardım') || text.includes('çağır')) {
            return 'HELP';
        }
        if (text.includes('alışveriş') || text.includes('başla') || text.includes('kamera')) {
            return 'SHOPPING';
        }
        if (text.includes('ayarlar')) {
            return 'SETTINGS';
        }
        if (text.includes('profil')) {
            return 'PROFILE';
        }

        return null;
    }
}

export default new VoiceService();
