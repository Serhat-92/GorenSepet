import React, { useState } from 'react';
import {
    View,
    Text,
    TextInput,
    TouchableOpacity,
    StyleSheet,
    Alert,
    KeyboardAvoidingView,
    Platform,
    SafeAreaView,
    ScrollView
} from 'react-native';
import { colors, spacing, typography, shadows, layout } from '../theme/theme';
import { supabase } from '../services/supabase';

export default function LoginScreen({ navigation }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        if (!email || !password) {
            Alert.alert('Eksik Bilgi', 'Lütfen giriş yapmak için e-posta ve şifrenizi girin.');
            return;
        }
        
        const { error } = await supabase.auth.signInWithPassword({ email, password });

        if (error) {
            Alert.alert('Giriş Hatası', error.message);
        } else {
            navigation.replace('Home');
        }
    };

    const handleRegister = async () => {
        if (!email || !password) {
            Alert.alert('Eksik Bilgi', 'Lütfen kayıt olmak için e-posta ve şifrenizi girin.');
            return;
        }

        const { error } = await supabase.auth.signUp({ email, password });

        if (error) {
            Alert.alert('Kayıt Hatası', error.message);
        } else {
            Alert.alert('Kayıt Başarılı', 'Devam etmek için giriş yapabilirsiniz.');
        }
    };

    return (
        <SafeAreaView style={styles.container}>
            <KeyboardAvoidingView
                behavior={Platform.OS === "ios" ? "padding" : "height"}
                style={styles.keyboardView}
            >
                <ScrollView contentContainerStyle={styles.innerContainer} accessible={true} accessibilityLabel="Giriş Ekranı">
                    <View style={styles.headerContainer}>
                        <Text style={styles.appName} accessibilityRole="header">GörenSepet</Text>
                        <Text style={styles.subtitle}>Engelsiz Alışverişin Adresi</Text>
                    </View>

                    <View style={styles.formContainer}>
                        <Text style={styles.label}>E-posta</Text>
                        <TextInput
                            style={styles.input}
                            placeholder="ornek@email.com"
                            placeholderTextColor={colors.textLight}
                            value={email}
                            onChangeText={setEmail}
                            keyboardType="email-address"
                            autoCapitalize="none"
                            accessibilityLabel="E-posta giriş alanı"
                            accessibilityHint="E-posta adresinizi girin"
                        />

                        <Text style={styles.label}>Şifre</Text>
                        <TextInput
                            style={styles.input}
                            placeholder="******"
                            placeholderTextColor={colors.textLight}
                            value={password}
                            onChangeText={setPassword}
                            secureTextEntry
                            accessibilityLabel="Şifre giriş alanı"
                            accessibilityHint="Şifrenizi girin"
                        />

                        <TouchableOpacity
                            style={styles.loginButton}
                            onPress={handleLogin}
                            activeOpacity={0.8}
                            accessibilityRole="button"
                            accessibilityLabel="Giriş Yap"
                            accessibilityHint="Ana sayfaya yönlendirir"
                        >
                            <Text style={styles.loginButtonText}>Giriş Yap</Text>
                        </TouchableOpacity>

                        <TouchableOpacity
                            style={styles.registerButton}
                            onPress={handleRegister}
                            accessibilityRole="button"
                            accessibilityLabel="Kayıt Ol"
                            accessibilityHint="Yeni hesap oluşturur"
                        >
                            <Text style={styles.registerButtonText}>Hesabınız yok mu? <Text style={styles.registerHighlight}>Kayıt Olun</Text></Text>
                        </TouchableOpacity>
                    </View>
                </ScrollView>
            </KeyboardAvoidingView>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: colors.background,
    },
    keyboardView: {
        flex: 1,
        justifyContent: 'center',
    },
    innerContainer: {
        flexGrow: 1,
        justifyContent: 'center',
        padding: spacing.large,
    },
    headerContainer: {
        alignItems: 'center',
        marginBottom: spacing.xxlarge,
    },
    appName: {
        ...typography.header,
        color: colors.primary,
        marginBottom: spacing.small,
    },
    subtitle: {
        ...typography.subheader,
        fontSize: 18,
        color: colors.textLight,
        fontWeight: 'normal',
    },
    formContainer: {
        backgroundColor: colors.surface,
        borderRadius: layout.borderRadius,
        padding: spacing.large,
        ...shadows.medium,
    },
    label: {
        ...typography.caption,
        color: colors.text,
        fontWeight: '600',
        marginBottom: spacing.tiny,
        marginLeft: spacing.small,
    },
    input: {
        backgroundColor: colors.background,
        height: layout.inputHeight,
        borderRadius: layout.borderRadius,
        paddingHorizontal: spacing.medium,
        marginBottom: spacing.medium,
        fontSize: 16,
        color: colors.text,
        borderWidth: 1,
        borderColor: colors.border,
    },
    loginButton: {
        backgroundColor: colors.primary,
        height: layout.inputHeight,
        borderRadius: layout.borderRadius,
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: spacing.small,
        ...shadows.small,
    },
    loginButtonText: {
        ...typography.button,
    },
    registerButton: {
        marginTop: spacing.large,
        alignItems: 'center',
    },
    registerButtonText: {
        fontSize: 14,
        color: colors.textLight,
    },
    registerHighlight: {
        color: colors.primary,
        fontWeight: 'bold',
    },
});
