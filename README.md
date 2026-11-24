# Tugas Praktek 9 - REST API Node-RED untuk Sistem IoT

**Nama:** Almas Yuri Aprilian
**NPM:** 2410020106
**Prodi:** Sistem Informasi
**Mata Kuliah:** Pemrograman Internet of Things

## Deskripsi
Sistem monitoring dan kontrol IoT sederhana:
sensor (simulasi ESP32) -> MQTT (Mosquitto) -> Node-RED (REST API) -> Dashboard web (HTML/CSS/JS).

## Isi Repository
| File | Fungsi |
|---|---|
| `flows.json` | Flow Node-RED: simulator sensor, subscribe MQTT, endpoint REST API |
| `dashboard.html` | Dashboard web yang mengambil data lewat REST API |
| `simulasi_esp32.py` | Simulator ESP32 versi Python (alternatif) |
| `kode_validasi_publish.js` | Kode function node untuk endpoint POST /api/kontrol |

## Endpoint
| Endpoint | Method | Fungsi |
|---|---|---|
| `/api/suhu` | GET | Data sensor terakhir |
| `/api/history` | GET | 50 data sensor terakhir |
| `/api/kontrol` | POST | Kirim perintah ke perangkat (body JSON: `device`, `action`) |

## Fitur Tambahan (Nilai Tambah)
- Grafik real-time suhu dan kelembaban menggunakan Chart.js di dashboard.
- Autentikasi sederhana: semua endpoint `/api/*` wajib header `X-API-Key` (salah/tidak ada = HTTP 401).
  Key hanya untuk keperluan belajar; pada sistem nyata simpan key di environment variable.
- Dashboard disajikan langsung oleh Node-RED (`httpStatic`) di `http://localhost:1880/dashboard.html`.

## Cara Menjalankan
1. Pastikan Mosquitto berjalan di `localhost:1883`.
2. Jalankan Node-RED (`node-red`), buka `http://127.0.0.1:1880`.
3. Menu Import, pilih `flows.json`, lalu Deploy.
4. Buka `dashboard.html` di browser.

## Uji Endpoint
```
curl -H "X-API-Key: iot-2410020106" http://localhost:1880/api/suhu
curl -H "X-API-Key: iot-2410020106" http://localhost:1880/api/history
curl -X POST -H "X-API-Key: iot-2410020106" http://localhost:1880/api/kontrol -d "{\"device\":\"lamp\",\"action\":\"on\"}"
curl http://localhost:1880/api/suhu   # tanpa key -> 401
```

## Screenshot
Tambahkan screenshot hasil pengujian di folder `screenshots/`.
