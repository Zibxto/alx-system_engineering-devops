# Commandline Challenge
## CMD CHALLENGE is an online game on Bash skills. Everything is done via the command line on the website and the questions become increasingly more complicated. It’s good training to improve command line skills. Each file shows the challenges I've completed.

## Steps to Use SFTP

1. **Establish an SFTP Session:** Open a terminal or command prompt and issue the following command, replacing `username` with your actual username and `serverip` with the server's IP address or hostname.
    ```
    sftp username@serverip
    ```

2. **Navigate to the Desired Directory:** Use the `cd` command to navigate to the directory on the remote server where you want to upload your files.
    ```
    cd path
    ```

3. **Upload Files:** To upload files from your local system to the remote server, use the `put` command followed by the filename. Replace `filename` with the actual name of the file you want to upload.
    ```
    put filename
    ```

4. **Exit SFTP Session:** When you're done uploading files and want to exit the SFTP session, use the following command:
    ```
    exit
    ```

These steps will allow you to securely transfer files to the remote server using SFTP.

