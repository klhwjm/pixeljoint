Pixeljoint artists scrapper made on python.

## Usage

### Arguments

- `-o, --output`: The output folder where downloaded artists will be saved.
- `-a, --archive`: Archive file to keep track of downloads for periodic updates.
- `profile_list`: A text file containing a list of Pixeljoint profile URLs.

### Example Command

profile_list_file.txt (dummy file)
`
https://pixeljoint.com/p/7755.htm\n
https://pixeljoint.com/p/6741.htm
`

```bash
pixeljoint -o PATH -a archive.txt profile_list_file.txt

