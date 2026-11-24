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
| `/api/threshold` | GET / PUT | Baca / ubah batas suhu (body JSON: `batas`) |
| `/api/kontrol` | POST | Kirim perintah ke perangkat (body JSON: `device`, `action`) |

## Fitur Tambahan (Nilai Tambah)
- Grafik real-time suhu dan kelembaban menggunakan Chart.js di dashboard.
- Autentikasi sederhana: semua endpoint `/api/*` wajib header `X-API-Key` (salah/tidak ada = HTTP 401).
  Key hanya untuk keperluan belajar; pada sistem nyata simpan key di environment variable.
- Endpoint `/api/threshold` (PUT) untuk mengatur batas suhu, dan GET untuk membaca batas. Saat suhu melewati batas,
  flow mengirim notifikasi ke topik MQTT `iot/notifikasi`, tampil di panel Debug Node-RED, dan dashboard menampilkan banner peringatan.
- WebSocket (`ws://localhost:1880/ws/sensor`): data sensor didorong langsung dari Node-RED ke dashboard tanpa polling.
  Polling REST API hanya berjalan sebagai cadangan jika WebSocket terputus.
  Catatan: WebSocket di browser tidak bisa mengirim header `X-API-Key`, sehingga jalur ini hanya untuk data baca (tanpa key).
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
curl -X PUT -H "X-API-Key: iot-2410020106" http://localhost:1880/api/threshold -d "{\"batas\":28}"
curl http://localhost:1880/api/suhu   # tanpa key -> 401
```

## Screenshot
Disertakan Screenshot di setiap pengerjaan.
