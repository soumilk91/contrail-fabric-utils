traffic_servers = {
    '192.168.2.253' : {'tcp': ['9100', '9101', '9102'], 'udp': ['9200', '9201']},
    '192.168.2.252' : {'tcp': ['9100', '9101', '9102'], 'udp': ['9200', '9201']},
}

traffic_clients = {
    '192.168.1.253' :
      {
	'192.168.2.253' : {'tcp': ['9100', '9101'], 'udp': ['9200']},
        '192.168.2.252' : {'tcp': ['9100', '9101', '9102'], 'udp': ['9200', '9201']}
	},

    '192.168.1.252' :
      {
	'192.168.2.253' : {'tcp': ['9100', '9101'], 'udp': ['9200']},
        '192.168.2.252' : {'tcp': ['9100', '9101', '9102'], 'udp': ['9200', '9201']}
	},
}
