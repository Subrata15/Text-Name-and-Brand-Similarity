class Task1():
    print('This function used to find similarities and classify similarity by treshold \nTreshold set in the cosine_tres function, please be check')
    # NOTE : YOU CAN CUSTOM VALUE OF TRESHOLD BY YOUR SELF
    # treshold set in the cosine_tres function, please be check
    # *** If want to know how cosine similarity used in this project, you can check in the cosine_function.ipynb file ***

    def __init__(self, df, kolom_search, kolom_loc):
        self.df=df
        self.kolom_search=kolom_search
        self.kolom_loc=kolom_loc
    
    def txt_lower(self,_txt):
        search_lower = list(_txt.split(" ")) 
        return search_lower 
    
    def _gettxtlist(self,df,na_kolom):
        df[na_kolom] = df[na_kolom].astype(str) 
        # ...Warning : in default we set into str
        txt_list = df[na_kolom].tolist()
        return txt_list
    
    def close_iter(self,loc,search):
        # *** import difflib ***
        import difflib as dgx
        temp_list = []
        for i in loc:
            temp_ = dgx.get_close_matches(i, search,1, 0.72)
            if temp_ != list():
                temp_list.append(temp_[-1])
            else:
                pass
        return temp_list
    
    def match_calc(self, calc_, loc, search):
        
        if len(loc) > len(search):
            return 'Maybe Close Matching, but we decide as not'
        elif calc_ > 80: 
            #... This treshold must be check in the future
            return 'Close Matching'
        elif calc_ < 70:
            return 'Not Close Matching'
        else:
            return 'Confusing'
        

    def get_cosine(self, vec1, vec2):
        import math
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
        sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator
    
    def text_to_vector(self, text):
        import re
        WORD = re.compile(r"\w+")
        
        from collections import Counter
        words = WORD.findall(text)
        return Counter(words)
    
    def cosine_tres(self, cosine_score):
        if cosine_score > 90: 
            # ...This treshold must be check in the future
            return 'Similar'
        else:
            return 'Not Similar'
    
    def similar(self):
        df = self.df
        kolom_loc=self.kolom_loc
        search_txt=self.kolom_search
        
        loc_list = self._gettxtlist(df, kolom_loc)
        search_list = self._gettxtlist(df, search_txt)
        
        match_temp = []
        cosine_temp = []
        temp_calc_ = []
        try:
            
            for diu,iu in enumerate(loc_list):
                search_pattern = self.txt_lower(search_list[diu])
                
                loc_ = self.txt_lower(iu)
                temp_get = self.close_iter(loc_, search_pattern)
                
                # calculate close match
                calc_ = (len(temp_get)/len(search_pattern))*100
                # Get Close Match Method
                match_temp.append(self.match_calc(calc_, loc_, search_pattern))
                
                # get cosine similarity
                vector1 = self.text_to_vector(search_list[diu]) 
                #*
                vector2 = self.text_to_vector(iu) 
                #*
                
                cosine = self.get_cosine(vector1, vector2)
                calc_cosine = cosine*100
                
                # Cosine Similarity
                cosine_temp.append(self.cosine_tres(calc_cosine))
                temp_calc_.append(calc_cosine)
            
            return match_temp, cosine_temp, temp_calc_

        except Exception as e:
            import sys
            import os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            error_msg = [e,exc_type,exc_tb.tb_lineno]
            
            for i in error_msg:
                print('Exception message: ', i)
                
            return 'Not OK'