class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        src_len = len(str1)
        tgt_len = len(str2)
        src_idx = 0
        tgt_idx = 0
        
        while src_idx < src_len and tgt_idx < tgt_len:
            if (str1[src_idx] == str2[tgt_idx] or 
                (str1[src_idx] == 'z' and str2[tgt_idx] == 'a') or 
                (ord(str1[src_idx]) + 1 == ord(str2[tgt_idx]))):
                src_idx += 1
                tgt_idx += 1
            else:
                src_idx += 1
                
        return tgt_idx == tgt_len