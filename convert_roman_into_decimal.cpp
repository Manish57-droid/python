#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,ans=0;
	string s;
	cin>>s;
	unordered_map<char,int>mp;
	mp['I']=1;
	mp['V']=5;
	mp['X']=10;
	mp['L']=50;
	mp['C']=100;
	mp['D']=500;
	mp['M']=1000;
	
	for(i=0;i<s.length();i++)
	{
		if(i==s.length()-1)
		cout<<mp[s[i]];
		else if(i+1<s.length() && mp[s[i+1]]>mp[s[i]])
		{
			ans+=mp[s[i+1]]-mp[s[i]];
			i+=1;
		}
		else
		{
			ans+=mp[s[i]];
		}
	}
	cout<<ans;
}
