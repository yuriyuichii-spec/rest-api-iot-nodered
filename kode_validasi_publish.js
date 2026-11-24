var body = msg.payload;

// Body bisa berupa Buffer, teks JSON, atau objek
if (Buffer.isBuffer(body)) body = body.toString();
if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = null; }
}

if (!body || !body.device || !body.action) {
    msg.statusCode = 400;
    msg.payload = {status: 'error', message: 'device dan action wajib diisi'};
    msg.headers = {'Access-Control-Allow-Origin': '*'};
    return [msg, null];
}

// Kirim perintah ke MQTT (output 2)
var mqttMsg = {payload: body, topic: 'iot/kontrol'};

msg.statusCode = 200;
msg.payload = {status: 'success', message: 'Perintah terkirim', sent: body};
msg.headers = {'Access-Control-Allow-Origin': '*'};
return [msg, mqttMsg];