You are given a string "str". Find the maximum number of non-empty substrings of "str" such that no two substrings overlap with each other and each substring that you select containing a letter 't' must contain all the occurrences of 't' in that substring. A string 'a' is a substring of a string 'b' if 'a' can be obtained from 'b' by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

#include<bits/stdc++.h>
int getEnd(vector<int>&l,vector<int>&r,int ind,string&str){
    int right=r[str[ind]-'a'];
    for(int i=ind;i<=right;i++){
        if(l[str[i]-'a']<ind)return -1;
        right=max(right,r[str[i]-'a']);
    }
    return right;
}
vector<string> nonOverlappingSubstrings(string &str) {
    vector<int>l(26,INT_MAX),r(26,INT_MIN);
    for(int i=0;i<str.size();i++){
        l[str[i]-'a']=min(i,l[str[i]-'a']);
        r[str[i]-'a']=i;
    }
    int right=-1;
    vector<string>res;
    for(int i=0;i<str.size();i++){
        if(l[str[i]-'a']==i){
            int newRight=getEnd(l,r,i,str);
            if (newRight != -1) {
              if (i > right)
                res.push_back("");
              right = newRight;
              res.back() = str.substr(i, right-i+1);
            }
        }
    }
    return res;
}