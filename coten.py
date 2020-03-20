import sys, quoter, renderer

def main(argv):
  quote = quoter.fetch_kindle()
  renderer.create(quote)

if __name__ == "__main__":
  main(sys.argv[1:])
