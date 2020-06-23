#import sys, quoter, renderer
import sys, quoter

def main(argv):
  quote = quoter.fetch_kindle()
  #renderer.create(quote)
  #renderer.create_pimoroni(quote)

if __name__ == "__main__":
  main(sys.argv[1:])
