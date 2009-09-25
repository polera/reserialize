from csv import reader
from json import dumps

class csv2json(object):
  """Convert CSV to JSON"""
  def __init__(self, infile, header_row=None):
    super(csv2json, self).__init__()
    self.header_row = header_row
    self.infile     = infile
  
  def get_max_items(self):
    """Get maximum items in any given row.  
       This sets the column headers/keys if
       none are given."""
    item_counts = []
    for line in reader(open(self.infile)):
      item_counts.append(len(line))
    return max(item_counts) + 1
    
  def generate(self, print_results=False):
    """Generate JSON from CSV"""
    json_temp_list = []
    row_counter = 0
    headers = []
    
    for line in reader(open(self.infile)):
      row_counter += 1
      if self.header_row is not None:
        if row_counter == self.header_row:
          headers = line
          continue
        elif row_counter < self.header_row:
          continue
      elif self.header_row is None and len(headers)==0:
        # No headers, assign some
        if row_counter == 1:
          for i in range(1,self.get_max_items()):
            headers.append("column%d" % i)
      else:
        pass
      line = iter(line)
      json = {}
      
      if line.__length_hint__() == 0:
        continue
      for key in headers:
          json[key] = line.next()

      json_temp_list.append(json)
    final_json = dumps(json_temp_list)
    if print_results:
      print final_json
    return final_json
    
    
  
