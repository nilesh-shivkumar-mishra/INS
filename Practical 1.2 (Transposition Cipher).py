import math
def get_column_read_order(key_str):
    key_info_with_original_indices = [(char, i) for i, char in enumerate(key_str)]
    sorted_key_info = sorted(key_info_with_original_indices)
    column_order = [info[1] for info in sorted_key_info]
    return column_order
def encryptMessage(msg, key):
    cipher_chars = []
    msg_list = list(msg)
    num_cols = len(key)
    num_rows = math.ceil(len(msg_list) / num_cols)
    num_padding = (num_rows * num_cols) - len(msg_list)
    msg_list.extend(['X'] * num_padding)  
    matrix = [msg_list[i:i + num_cols] for i in range(0, len(msg_list), num_cols)]
    column_read_order = get_column_read_order(key)
    for original_col_idx in column_read_order:
        for r in range(num_rows):
            cipher_chars.append(matrix[r][original_col_idx])
    return "".join(cipher_chars)
if __name__ == "__main__": 
    msg_to_encrypt = "NetworkSecurity"
    encryption_key = "TYCS"
    print(f"Original Message: {msg_to_encrypt}")
    print(f"Key: {encryption_key}")
    encrypted_text = encryptMessage(msg_to_encrypt, encryption_key)
    print(f"Encrypted Message: {encrypted_text}")
