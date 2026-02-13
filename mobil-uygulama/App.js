import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { useEffect, useState } from 'react';
import { supabase } from './src/services/supabase';

export default function App() {
  const [message, setMessage] = useState('Bağlanıyor...');
  const [productCount, setProductCount] = useState(0);

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    try {
      // 1. Ürün sayısını çekiyoruz
      const { count, error } = await supabase
        .from('products')
        .select('*', { count: 'exact', head: true });

      if (error) throw error;

      setProductCount(count);
      setMessage('✅ Supabase Bağlantısı ve Kütüphane Aktif!');
    } catch (e) {
      setMessage('❌ Hata: ' + e.message);
    }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Engelsiz Alışveriş</Text>
      <Text style={styles.status}>{message}</Text>
      <Text style={styles.count}>Veritabanındaki Ürün Sayısı: {productCount}</Text>
      <Text style={styles.info}>
        (Sayı 0 ise Supabase SQL Editor'den 'select insert_dummy_products();' komutunu çalıştırabilirsin)
      </Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#333',
  },
  status: {
    fontSize: 18,
    fontWeight: '600',
    color: '#007AFF',
    marginBottom: 10,
    textAlign: 'center',
  },
  count: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#2c3e50',
    marginBottom: 20,
  },
  info: {
    fontSize: 14,
    color: '#7f8c8d',
    textAlign: 'center',
    marginTop: 10,
  },
});
