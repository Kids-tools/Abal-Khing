import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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')))
