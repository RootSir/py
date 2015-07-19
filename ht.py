import urllib2

opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'https': 'http://:@117.165.15.215:3128'}))
                #urllib2.ProxyHandler({'https': 'http://:@218.193.132.35:808'}))
urllib2.install_opener(opener)
print urllib2.urlopen('https://iforgot.apple.com/password/verify/appleid',data,10).read()
ifeprint urllib2.urlopen('https://iforgot.apple.com/password/verify/appleid',data,10).read()
ifeprint urllib2.urlopen('https://iforgot.apple.com/password/verify/appleid',data,10).read()
ifeprint urllib2.urlopen('https://iforgot.apple.com/password/verify/appleid',data,10).read()
