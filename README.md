# m9

1. Clone this repository.
```bash
git clone https://github.com/Moses-93/m9.git
```

2. Create the .env file in the root directory of the project.
```bash
sudo touch .env
```

3. Add your MongoDB Atlas URI to the .env file: 
```bash
URL=mongodb+srv://yourname:yourpassword@cluster.gcs0k.mongodb.net/?retryWrites=true&w=majority&appName=Notes
```

4. Install the required dependencies:
```bash
poetry install
```

## Commands:

Run scraping
```bash
python main.py scrape
```
Run loading data to the database
```bash
python main.py load
```
Run searching data to the database
```bash
python main.py search
```