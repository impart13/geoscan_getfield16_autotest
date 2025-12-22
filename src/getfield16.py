import sys

def getfield16(hex_string, start_bit):
    
    try:
        #Преобразование hex-строки
        hex_string = hex_string.upper()
        if hex_string.startswith("0X"):
            hex_string = hex_string[2:]
        
        # Проверка на hex-символы
        valid_simbol = set("0123456789ABCDEF")
        if not all(simbol in valid_simbol for simbol in hex_string):
            raise ValueError("hex-строка содержит не корректные символы")
            
        # Проверка длинны
        if len(hex_string) > 32:
            raise ValueError("hex-строка слишком длинная")
            
        # Проверка start_bit
        try:
            start_bit = int(start_bit)
        except ValueError:
            return "Error: некорректный стартовый бит"
            
        if (start_bit < 0) or (start_bit > len(binary_str) - 16):
            raise ValueError("некорректный стартовый бит")
            
        # Преобраование hex-строки в бинарную
        binary_str = ""
        for simbol in hex_string:
            binary_str += format(int(simbol, 16), '04b')
            
        # Разбиваем на группы по 4 бита
        hex_result = ""
        binary_bits = binary_str[start_bit:start_bit + 16]
        for i in range(0, 16, 4):
            bits = binary_bits[i:i+4]
            hex_result += format(int(bits, 2), 'X')
            
        return hex_result
        
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    if len(sys.argv) != 3:
        print("Некорректное кол-во аргументов.")
        sys.exit(1)
        
    result = getfield16(sys.argv[1], sys.argv[2])
    print(result)

if __name__ == "__main__":
    main()