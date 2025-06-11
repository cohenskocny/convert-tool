# convert-tool

A simple command-line tool for converting between binary, hexadecimal, and raw bytes.

## 🔧 Usage

Make sure `convert.py` is executable:

```bash
chmod +x convert.py
```

Then run it like this:

### ➤ Convert binary to hex

```bash
./convert.py -b 1110010011011001100000101101110111111010101111001100010010011001
```

**Output:**
```
Hex:   e4d982ddfabcc499
Bytes: b'\xe4\xd9\x82\xdd\xfa\xbc\xc4\x99'
```

### ➤ Convert hex to binary

```bash
./convert.py -x e4d982ddfabcc499
```

**Output:**
```
Binary: 1110010011011001100000101101110111111010101111001100010010011001
Bytes:  b'\xe4\xd9\x82\xdd\xfa\xbc\xc4\x99'
```

## 🛠️ Optional: Install for Global Use

If you'd like to use it like a real command:

```bash
sudo cp convert.py /usr/local/bin/convert
```

Now you can run:

```bash
convert -x deadbeef
```

from anywhere on your system.
