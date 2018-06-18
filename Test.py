def xor_two_str(data, key, block_size=None):
    xored = ""
    if (block_size is None):
        for i in range(max(len(data), len(key))):
            xored_value = ord(data[i % len(data)]) ^ ord(key[i % len(key)])
            xored += chr(xored_value)
    return xored


xor_res = xor_two_str("123456789", "aa")
print(xor_res)
print(xor_two_str(xor_res, "aa"))
