import cryptographicRatchets


s1 = cryptographicRatchets.Axolotl('Sensor1',dbname='axolotl1.db', dbpassphrase=None, nonthreaded_sql=False)
s2 = cryptographicRatchets.Axolotl('Sensor2',dbname='axolotl2.db', dbpassphrase=None, nonthreaded_sql=False)

    
s1.initState('Sensor2',s2.state['DHIs'], s2.handshakePKey, s2.state['DHRs'], verify=False)
s2.initState('Sensor1',s1.state['DHIs'], s1.handshakePKey, s1.state['DHRs'], verify=False)


# '--------Sensor1---(1)------'
s1.conversation
# '--------Sensor2---(1)------'
s2.conversation
# '///////////////////////////'

ci1 = s1.encrypt('Hello')
pl1 = s2.decrypt(ci1)

# '--------Sensor1---(2)------'
s1.conversation
# '--------Sensor2---(2)------'
s2.conversation
# '///////////////////////////'

ci2 = s1.encrypt('How Are You?')
pl2 = s2.decrypt(ci2)

# '--------Sensor1---(3)------'
s1.conversation
# '--------Sensor2---(3)------'
s2.conversation
# '///////////////////////////'

ci3 = s2.encrypt('I Am Fine')
pl3 = s1.decrypt(ci3)

# '--------Sensor1---(4)------'
s1.conversation
# '--------Sensor2---(4)------'
s2.conversation
# '///////////////////////////'

ci4 = s2.encrypt('What About You?')
pl4 = s1.decrypt(ci4)

# '--------Sensor1---(5)------'
s1.conversation
# '--------Sensor2---(5)------'
s2.conversation
# '///////////////////////////'

ci5 = s1.encrypt('Thank You')
pl5 = s2.decrypt(ci5)

# '--------Sensor1---(6)------'
s1.conversation
# '--------Sensor2---(6)------'
s2.conversation
# '///////////////////////////'