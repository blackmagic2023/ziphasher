# ziphasher
ziphasher.py is a Python script that generates a hash from a password-protected ZIP file using zip2john and then attempts to crack the password using John the Ripper with a specified password list. This tool is useful for security professionals and enthusiasts who need to test the strength of ZIP file passwords.
Features

   - Generates a hash from a ZIP file using zip2john.
   - Uses John the Ripper to attempt to crack the password with a provided wordlist.
   - Outputs the results of the password cracking attempt.

## Prerequisites

   - Python 3.x
   - zip2john (part of John the Ripper suite)
   - John the Ripper

## Installing John the Ripper

On Debian-based systems, you can install John the Ripper using:

```sh
sudo apt-get install john
```

For other systems, refer to the official John the Ripper documentation.
Installing zip2john

zip2john is included with John the Ripper. Ensure it is accessible from your command line.
Usage

   - Clone the repository or download the ziphasher.py script.

   - Run the script with the following command:

```sh
    python3 ziphasher.py <zip_file_path> <hash_file_path> <password_list_path>
```

       - <zip_file_path>: The path to the password-protected ZIP file.
       - <hash_file_path>: The path to the file where the hash will be saved.
       - <password_list_path>: The path to the password list file to be used by John the Ripper.

## Example

```sh
python3 ziphasher.py secret.zip hash.txt passwords.txt
```

This command will:

   - Generate a hash from secret.zip and save it to hash.txt.
   - Use John the Ripper with the password list in passwords.txt to attempt to crack the password.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

   1. Fork the repository.
   2. Create your feature branch (git checkout -b feature/your-feature).
   3. Commit your changes (git commit -am 'Add some feature').
   4. Push to the branch (git push origin feature/your-feature).
   5. Create a new Pull Request.

## Acknowledgements

   - John the Ripper - A fast password cracker.
   - zip2john - Utility to convert ZIP file hashes for use with John the Ripper.

## Disclaimer

This tool is intended for educational and ethical testing purposes only. Do not use this tool for illegal activities. The author is not responsible for any misuse of this tool.
