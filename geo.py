import json
fname='/home/manish/twi23_bot/data/stream_IPL.json'
with open(fname,'r') as f:
    geo_data={"type":"FeatureCollection","features":[]}
    for line in f:
        tweet=json.loads(line)
        if tweet['coordinates']:
            geo_json_feature = {"type":"Feature","geometry":tweet['coordinates'],"properties":{"text":tweet['text'],"created_at":tweet['created_at']}}
            geo_data['features'].append(geo_json_feature)
            #print(geo_data)
            with open('/home/manish/twi23_bot/geo_data.json', 'w') as fout:
                fout.write(josn.dumps(geo_data,indent=4))
