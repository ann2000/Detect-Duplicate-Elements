
class DetectDuplicates:
    
    def __init__(self, input_list) -> None:
        
        self.input_list = input_list
        self.element_count = {}
        self.duplicate_list = []
    
    def detect_duplicate_elements(self):

        for element in input:
            if element in self.element_count:
                self.element_count[element] += 1
            else:
                self.element_count[element] = 1

        for element in self.element_count:
            if self.element_count[element] > 1:
                self.duplicate_list.append(element)
    
        return self.duplicate_list

if __name__ == "__main__":

    input = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
    detect_duplicates = DetectDuplicates(input)
    duplicate_list = detect_duplicates.detect_duplicate_elements()
    print(duplicate_list)
