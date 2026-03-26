const API_URL = process.env.EXPO_PUBLIC_AI_API_URL || 'http://10.0.2.2:8000';

class ApiService {
    /**
     * Kullanıcının sesli komutunu (örn: "kısır yapacağım") yapay zekaya gönderir
     * ve dönen malzeme listesini alır.
     * @param {string} text - Kullanıcının söylediği cümle
     * @returns {Promise<Object>} - { basarili: boolean, yemek: string, malzemeler: Array }
     */
    async parseRecipe(text) {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 saniye zaman aşımı

        try {
            const response = await fetch(`${API_URL}/api/parse-recipe`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ metin: text }),
                signal: controller.signal
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                throw new Error(`API isteği başarısız oldu: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            clearTimeout(timeoutId);
            console.error('Yapay Zeka API Hatası (parseRecipe):', error);
            
            let errorMessage = 'Yapay zeka asistanına şu an ulaşılamıyor. Lütfen internet veya sunucu bağlantınızı kontrol edin.';
            if (error.name === 'AbortError') {
                errorMessage = 'Sunucuya bağlanılırken zaman aşımına uğradı. Beklenenden uzun sürdü.';
            }

            // Default hata dönüşü
            return {
                basarili: false,
                mesaj: errorMessage
            };
        }
    }
}

export default new ApiService();
