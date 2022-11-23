from sklearn.tree import DecisionTreeClassifier
from micromlgen import port_wifi_indoor_positioning, port

if __name__ == '__main__':
    samples = '''
    {"__location": "Hall", "Grogu’s Temple": -76, "Telekom-ooMjjf": -76, "Pizza": -79, "STRONG_Bableves": -80, "STRONG_Kifli": -80, "Telekom-Yeg3O5": -82, "c67ace77": -83, "Telekom-Hotspot": -86, "Telekom-8Dxwfh": -86, "Vodafone-D76C": -86, "Telekom-94BCF8": -87, "STRONG_Kifli": -88, "STRONG_Bableves": -89, "": -90, "Telekom-iSOTvC": -91, "UPC8EDBB49": -92, "TG": -92, "Telekom-dcWZu9": -92, "Telekom-r6sGoX": -92, "Heni": -93, "Telekom-Vllhpb": -94, "Telekom-PPcFME": -94, "Telekom-Hotspot": -96}
{"__location": "Hall", "Telekom-ooMjjf": -77, "Grogu’s Temple": -78, "Pizza": -78, "c67ace77": -82, "STRONG_Bableves": -82, "STRONG_Kifli": -82, "Telekom-Yeg3O5": -82, "Telekom-8Dxwfh": -82, "STRONG_Kifli": -86, "Vodafone-D76C": -86, "Telekom-94BCF8": -87, "Telekom-Hotspot": -88, "Telekom-iSOTvC": -89, "": -90, "STRONG_Bableves": -92, "UPC8EDBB49": -92, "Telekom-rQs6gW": -92, "Telekom-Vllhpb": -92, "Telekom-2.4": -92, "Telekom-r6sGoX": -93, "Telekom-PPcFME": -96}
{"__location": "Hall", "Telekom-ooMjjf": -76, "STRONG_Kifli": -78, "Pizza": -79, "STRONG_Bableves": -80, "Grogu’s Temple": -80, "c67ace77": -81, "Telekom-Yeg3O5": -82, "Telekom-Hotspot": -84, "Telekom-94BCF8": -85, "Telekom-8Dxwfh": -85, "STRONG_Bableves": -88, "STRONG_Kifli": -88, "Vodafone-D76C": -89, "": -89, "Telekom-rQs6gW": -90, "Telekom-r6sGoX": -90, "Telekom-iSOTvC": -91, "dlink_121": -92, "TG": -92, "Telekom-dcWZu9": -92, "Telekom-PPcFME": -93, "Heni": -94, "Telekom-Vllhpb": -94}
{"__location": "Hall", "Grogu’s Temple": -77, "Telekom-ooMjjf": -78, "STRONG_Kifli": -80, "Pizza": -80, "Telekom-Yeg3O5": -80, "STRONG_Bableves": -81, "c67ace77": -82, "Telekom-8Dxwfh": -84, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "STRONG_Bableves": -88, "STRONG_Kifli": -89, "TG": -89, "Telekom-r6sGoX": -89, "": -89, "Telekom-rQs6gW": -90, "Telekom-iSOTvC": -91, "Vodafone-D76C": -92, "Telekom-Vllhpb": -92, "Telekom-PPcFME": -93, "Telekom-dcWZu9": -94, "Vodafone-7159": -95}
{"__location": "Hall", "Grogu’s Temple": -77, "STRONG_Bableves": -80, "STRONG_Kifli": -80, "Telekom-Yeg3O5": -80, "Telekom-ooMjjf": -80, "c67ace77": -81, "Telekom-Hotspot": -81, "Pizza": -81, "Telekom-8Dxwfh": -81, "Telekom-94BCF8": -82, "Telekom-iSOTvC": -86, "STRONG_Bableves": -88, "Vodafone-D76C": -88, "STRONG_Kifli": -89, "Telekom-2.4": -89, "Telekom-rQs6gW": -90, "Telekom-r6sGoX": -90, "": -90, "Telekom-Vllhpb": -92, "Heni": -94, "Telekom-dcWZu9": -94, "Liliom": -94}
{"__location": "Hall", "Pizza": -72, "Telekom-ooMjjf": -79, "Grogu’s Temple": -80, "STRONG_Bableves": -81, "c67ace77": -81, "STRONG_Kifli": -82, "Telekom-94BCF8": -82, "Telekom-Hotspot": -82, "Telekom-8Dxwfh": -82, "Telekom-Yeg3O5": -83, "STRONG_Bableves": -85, "STRONG_Kifli": -87, "Vodafone-D76C": -89, "": -90, "Telekom-iSOTvC": -91, "TG": -91, "Telekom-r6sGoX": -92, "Telekom-rQs6gW": -93, "Telekom-Vllhpb": -94}
{"__location": "Hall", "Pizza": -72, "Grogu’s Temple": -78, "c67ace77": -80, "Telekom-8Dxwfh": -80, "Telekom-ooMjjf": -81, "STRONG_Bableves": -82, "STRONG_Kifli": -82, "Telekom-94BCF8": -82, "Telekom-Hotspot": -82, "Telekom-Yeg3O5": -82, "Vodafone-D76C": -86, "STRONG_Bableves": -87, "STRONG_Kifli": -87, "Telekom-iSOTvC": -87, "Telekom-r6sGoX": -91, "": -91, "Telekom-rQs6gW": -92, "TG": -92, "Telekom-Vllhpb": -96}
{"__location": "Hall", "Pizza": -72, "c67ace77": -79, "Grogu’s Temple": -79, "Telekom-8Dxwfh": -80, "Telekom-ooMjjf": -80, "Telekom-Hotspot": -81, "Telekom-94BCF8": -82, "Telekom-Yeg3O5": -82, "Vodafone-D76C": -87, "Telekom-iSOTvC": -88, "STRONG_Bableves": -89, "STRONG_Bableves": -90, "STRONG_Kifli": -90, "": -90, "STRONG_Kifli": -91, "Telekom-rQs6gW": -91, "Heni": -95, "Telekom-Vllhpb": -97}
{"__location": "Hall", "Pizza": -78, "Telekom-ooMjjf": -78, "c67ace77": -80, "Grogu’s Temple": -80, "Telekom-8Dxwfh": -80, "STRONG_Kifli": -82, "STRONG_Bableves": -82, "Telekom-Yeg3O5": -84, "Telekom-Hotspot": -87, "STRONG_Kifli": -88, "Telekom-94BCF8": -88, "Telekom-rQs6gW": -88, "STRONG_Bableves": -89, "Telekom-iSOTvC": -89, "TG": -89, "Telekom-Vllhpb": -91, "": -91, "Telekom-687116": -92, "Vodafone-D76C": -92, "UPC8EDBB49": -93, "Vodafone-F39B": -94, "Telekom-2.4": -94, "Telekom-r6sGoX": -97}
{"__location": "Hall", "Grogu’s Temple": -77, "Pizza": -78, "Telekom-ooMjjf": -79, "c67ace77": -80, "STRONG_Bableves": -80, "STRONG_Kifli": -80, "Telekom-8Dxwfh": -82, "Telekom-94BCF8": -83, "Telekom-Hotspot": -84, "STRONG_Kifli": -86, "Telekom-iSOTvC": -86, "Telekom-Yeg3O5": -87, "Telekom-rQs6gW": -88, "STRONG_Bableves": -89, "UPC8EDBB49": -90, "Vodafone-D76C": -91, "Telekom-Vllhpb": -92, "Telekom-2.4": -92, "Telekom-r6sGoX": -93, "Vodafone-7159": -93, "": -93, "UPC7283307": -94, "Vodafone-F39B": -96}
{"__location": "Hall", "Telekom-ooMjjf": -75, "Pizza": -78, "c67ace77": -79, "Grogu’s Temple": -80, "Telekom-8Dxwfh": -80, "STRONG_Kifli": -81, "STRONG_Bableves": -81, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "Telekom-Yeg3O5": -85, "STRONG_Bableves": -87, "STRONG_Kifli": -87, "Telekom-iSOTvC": -88, "Telekom-rQs6gW": -89, "TG": -89, "Telekom-Vllhpb": -90, "UPC8EDBB49": -91, "": -91, "Telekom-7UNMPx": -93, "Telekom-r6sGoX": -93, "Vodafone-D76C": -93, "Telekom-2.4": -95, "Vodafone-F39B": -96}
{"__location": "Hall", "Telekom-ooMjjf": -77, "Pizza": -78, "Grogu’s Temple": -79, "STRONG_Bableves": -80, "STRONG_Kifli": -80, "c67ace77": -80, "Telekom-8Dxwfh": -82, "Telekom-Hotspot": -85, "STRONG_Bableves": -87, "Telekom-iSOTvC": -88, "Telekom-rQs6gW": -88, "Telekom-Yeg3O5": -88, "TG": -88, "STRONG_Kifli": -89, "Telekom-Vllhpb": -89, "Telekom-r6sGoX": -90, "": -90, "UPC8EDBB49": -91, "Vodafone-F39B": -93, "Telekom-2.4": -93, "Vodafone-D76C": -93, "UPC7283307": -94, "Telekom-Hotspot": -95}
{"__location": "Hall", "Pizza": -72, "Telekom-ooMjjf": -77, "c67ace77": -79, "STRONG_Bableves": -81, "STRONG_Kifli": -81, "Grogu’s Temple": -82, "Telekom-8Dxwfh": -82, "Telekom-94BCF8": -85, "Telekom-Hotspot": -86, "Telekom-iSOTvC": -86, "Telekom-rQs6gW": -87, "Telekom-Yeg3O5": -87, "STRONG_Bableves": -88, "STRONG_Kifli": -89, "TG": -90, "Telekom-Hotspot": -91, "Telekom-r6sGoX": -91, "Vodafone-D76C": -91, "Telekom-Vllhpb": -91, "": -91, "UPC8EDBB49": -92, "Telekom-687116": -92, "Telekom-7UNMPx": -92, "Heni": -93, "Telekom-2.4": -93, "Vodafone-F39B": -95}
{"__location": "Hall", "Pizza": -71, "Telekom-ooMjjf": -77, "c67ace77": -79, "STRONG_Kifli": -80, "STRONG_Bableves": -81, "Grogu’s Temple": -81, "Telekom-8Dxwfh": -82, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "STRONG_Bableves": -88, "Telekom-Yeg3O5": -88, "Telekom-rQs6gW": -88, "STRONG_Kifli": -89, "Telekom-iSOTvC": -89, "TG": -90, "Vodafone-D76C": -91, "": -91, "UPC8EDBB49": -92, "Telekom-687116": -92, "Telekom-r6sGoX": -92, "Telekom-Vllhpb": -92, "Telekom-2.4": -92, "Vodafone-F39B": -94, "UPC7283307": -96}
{"__location": "Hall", "Pizza": -71, "Telekom-ooMjjf": -77, "Grogu’s Temple": -79, "Telekom-8Dxwfh": -79, "c67ace77": -80, "STRONG_Kifli": -80, "STRONG_Bableves": -81, "Telekom-94BCF8": -86, "STRONG_Bableves": -87, "Telekom-Yeg3O5": -87, "STRONG_Kifli": -88, "TG": -89, "Telekom-r6sGoX": -89, "Telekom-Vllhpb": -90, "": -91, "UPC8EDBB49": -92, "Vodafone-F39B": -93, "Vodafone-D76C": -93, "Telekom-2.4": -95}
{"__location": "Hall", "Telekom-ooMjjf": -76, "Pizza": -78, "c67ace77": -79, "Telekom-8Dxwfh": -79, "STRONG_Bableves": -80, "STRONG_Kifli": -80, "Grogu’s Temple": -80, "Telekom-Yeg3O5": -85, "Telekom-Hotspot": -86, "STRONG_Bableves": -87, "STRONG_Kifli": -87, "Telekom-94BCF8": -87, "Telekom-iSOTvC": -89, "Telekom-rQs6gW": -89, "UPC8EDBB49": -90, "Telekom-r6sGoX": -90, "Telekom-Vllhpb": -90, "TG": -91, "": -91, "Vodafone-F39B": -93, "Vodafone-D76C": -93, "Telekom-Hotspot": -94, "Telekom-2.4": -94, "Vodafone-7159": -94}
{"__location": "Hall", "Telekom-ooMjjf": -77, "Pizza": -78, "c67ace77": -79, "Grogu’s Temple": -79, "STRONG_Kifli": -80, "STRONG_Bableves": -82, "Telekom-8Dxwfh": -82, "Telekom-Hotspot": -85, "Telekom-94BCF8": -86, "STRONG_Bableves": -87, "STRONG_Kifli": -87, "TG": -88, "Telekom-iSOTvC": -89, "Telekom-r6sGoX": -90, "Telekom-Vllhpb": -91, "": -92, "UPC8EDBB49": -93, "Telekom-1F4184": -93, "Vodafone-D76C": -93, "Telekom-7UNMPx": -94, "Telekom-2.4": -94, "Vodafone-F39B": -95}
{"__location": "Hall", "c67ace77": -75, "Grogu’s Temple": -77, "Pizza": -78, "Telekom-ooMjjf": -78, "STRONG_Bableves": -81, "STRONG_Kifli": -81, "Telekom-8Dxwfh": -81, "STRONG_Kifli": -85, "Telekom-94BCF8": -85, "Telekom-Hotspot": -86, "Telekom-iSOTvC": -87, "STRONG_Bableves": -88, "Telekom-rQs6gW": -88, "Telekom-Yeg3O5": -88, "Telekom-r6sGoX": -91, "Vodafone-D76C": -91, "Telekom-687116": -92, "Telekom-Vllhpb": -92, "": -92, "UPC8EDBB49": -93, "Telekom-Hotspot": -93, "Telekom-1F4184": -94, "Vodafone-F39B": -95, "UPC7283307": -96}
{"__location": "Hall", "Telekom-ooMjjf": -76, "Pizza": -78, "c67ace77": -79, "STRONG_Kifli": -80, "STRONG_Bableves": -80, "Grogu’s Temple": -81, "Telekom-8Dxwfh": -84, "STRONG_Bableves": -85, "Telekom-94BCF8": -86, "Telekom-Hotspot": -86, "STRONG_Kifli": -88, "Telekom-rQs6gW": -89, "Telekom-Yeg3O5": -89, "Telekom-iSOTvC": -89, "Telekom-r6sGoX": -90, "UPC8EDBB49": -91, "Telekom-687116": -92, "Vodafone-D76C": -92, "Telekom-Vllhpb": -92, "Telekom-7UNMPx": -93, "": -93, "Telekom-1F4184": -94, "Vodafone-F39B": -95, "Telekom-2.4": -96, "UPC7283307": -96}
{"__location": "Hall", "Telekom-ooMjjf": -75, "c67ace77": -77, "Grogu’s Temple": -77, "Pizza": -77, "STRONG_Kifli": -78, "STRONG_Bableves": -79, "Telekom-Hotspot": -84, "Telekom-8Dxwfh": -84, "Telekom-94BCF8": -85, "STRONG_Bableves": -86, "STRONG_Kifli": -87, "Telekom-rQs6gW": -87, "Telekom-Yeg3O5": -87, "Telekom-Hotspot": -89, "Telekom-iSOTvC": -90, "UPC8EDBB49": -90, "Telekom-r6sGoX": -90, "Telekom-Vllhpb": -90, "": -90, "Vodafone-F39B": -91, "Telekom-2.4": -92, "Telekom-687116": -93, "Telekom-1F4184": -93, "Vodafone-D76C": -93, "UPC7283307": -95}
{"__location": "Hall", "Telekom-ooMjjf": -76, "c67ace77": -78, "STRONG_Bableves": -78, "STRONG_Kifli": -78, "Pizza": -78, "Grogu’s Temple": -80, "Telekom-8Dxwfh": -81, "Telekom-94BCF8": -84, "Telekom-Hotspot": -85, "STRONG_Kifli": -87, "Telekom-iSOTvC": -87, "Telekom-rQs6gW": -87, "STRONG_Bableves": -88, "Telekom-Yeg3O5": -88, "Telekom-1F4184": -90, "Telekom-r6sGoX": -90, "Vodafone-D76C": -90, "Telekom-2.4": -90, "Telekom-687116": -91, "Telekom-Hotspot": -91, "": -91, "Telekom-Vllhpb": -92, "Vodafone-7159": -92, "UPC8EDBB49": -93, "Vodafone-F39B": -95, "UPC7283307": -96}
{"__location": "Hall", "Grogu’s Temple": -77, "Telekom-ooMjjf": -77, "c67ace77": -78, "Pizza": -78, "STRONG_Bableves": -79, "STRONG_Kifli": -79, "TG": -84, "Telekom-8Dxwfh": -85, "Telekom-94BCF8": -86, "Telekom-Hotspot": -86, "Telekom-rQs6gW": -86, "Telekom-Yeg3O5": -87, "STRONG_Bableves": -88, "STRONG_Kifli": -89, "Telekom-687116": -89, "Telekom-2.4": -89, "Telekom-iSOTvC": -90, "Vodafone-D76C": -90, "UPC8EDBB49": -91, "Telekom-r6sGoX": -91, "": -91, "Telekom-Hotspot": -92, "Telekom-Vllhpb": -93, "Vodafone-7159": -95, "Vodafone-F39B": -96}
{"__location": "Hall", "Telekom-ooMjjf": -75, "Pizza": -76, "Grogu’s Temple": -78, "c67ace77": -79, "STRONG_Bableves": -79, "STRONG_Kifli": -79, "Telekom-8Dxwfh": -83, "Telekom-94BCF8": -84, "Telekom-Hotspot": -85, "STRONG_Bableves": -87, "Telekom-iSOTvC": -87, "STRONG_Kifli": -88, "Telekom-rQs6gW": -88, "TG": -88, "Telekom-Yeg3O5": -89, "": -90, "Vodafone-F39B": -91, "Telekom-Vllhpb": -91, "Telekom-687116": -92, "Vodafone-7159": -92, "Telekom-2.4": -92, "UPC8EDBB49": -93, "Telekom-r6sGoX": -93, "Vodafone-D76C": -93, "UPC7283307": -95}
{"__location": "Hall", "Telekom-ooMjjf": -77, "Grogu’s Temple": -78, "STRONG_Bableves": -78, "c67ace77": -78, "STRONG_Kifli": -80, "Telekom-Yeg3O5": -81, "Telekom-94BCF8": -85, "Telekom-8Dxwfh": -85, "Telekom-Hotspot": -86, "STRONG_Kifli": -87, "STRONG_Bableves": -88, "Telekom-rQs6gW": -88, "Telekom-iSOTvC": -89, "Telekom-r6sGoX": -89, "": -91, "UPC8EDBB49": -92, "Vodafone-D76C": -92, "Telekom-2.4": -93, "Telekom-Vllhpb": -94, "Vodafone-F39B": -95, "UPC7283307": -96}
{"__location": "Hall", "Pizza": -72, "Telekom-ooMjjf": -77, "c67ace77": -78, "STRONG_Kifli": -80, "STRONG_Bableves": -80, "Grogu’s Temple": -82, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "Telekom-8Dxwfh": -86, "STRONG_Kifli": -87, "Telekom-Yeg3O5": -87, "STRONG_Bableves": -88, "Telekom-iSOTvC": -89, "TG": -91, "Telekom-r6sGoX": -91, "Vodafone-7159": -91, "Vodafone-D76C": -91, "": -91, "UPC8EDBB49": -92, "Vodafone-F39B": -92, "Telekom-1F4184": -93, "Telekom-Hotspot": -93, "Telekom-2.4": -93, "T-965259": -94, "UPC7283307": -94, "Telekom-Vllhpb": -95}
{"__location": "Hall", "Telekom-ooMjjf": -77, "STRONG_Kifli": -78, "Pizza": -78, "c67ace77": -79, "STRONG_Bableves": -79, "Grogu’s Temple": -82, "Telekom-8Dxwfh": -83, "Telekom-Hotspot": -85, "Telekom-94BCF8": -85, "STRONG_Bableves": -86, "STRONG_Kifli": -88, "Telekom-iSOTvC": -88, "Telekom-Yeg3O5": -88, "UPC8EDBB49": -91, "Telekom-Hotspot": -91, "": -91, "Vodafone-D76C": -92, "Telekom-1F4184": -93, "Telekom-7UNMPx": -94, "Telekom-r6sGoX": -94, "Telekom-Vllhpb": -94, "Telekom-2.4": -94, "Vodafone-7159": -95}
{"__location": "Hall", "Telekom-ooMjjf": -76, "c67ace77": -78, "Grogu’s Temple": -78, "Pizza": -78, "STRONG_Kifli": -79, "STRONG_Bableves": -79, "Telekom-8Dxwfh": -81, "Telekom-Yeg3O5": -83, "Telekom-Hotspot": -85, "Telekom-94BCF8": -86, "STRONG_Bableves": -87, "STRONG_Kifli": -87, "Telekom-iSOTvC": -88, "Telekom-1F4184": -90, "Vodafone-D76C": -90, "Telekom-Hotspot": -91, "Telekom-r6sGoX": -91, "": -91, "Vodafone-7159": -92, "Telekom-Vllhpb": -93, "Telekom-2.4": -94}
{"__location": "Hall", "Pizza": -71, "c67ace77": -77, "STRONG_Bableves": -79, "STRONG_Kifli": -79, "Grogu’s Temple": -79, "Telekom-ooMjjf": -79, "Telekom-Yeg3O5": -82, "Telekom-Hotspot": -85, "Telekom-94BCF8": -86, "Telekom-8Dxwfh": -86, "STRONG_Bableves": -87, "Telekom-rQs6gW": -87, "STRONG_Kifli": -88, "TG": -89, "Telekom-iSOTvC": -90, "Telekom-Hotspot": -90, "Vodafone-D76C": -90, "Telekom-Vllhpb": -90, "UPC8EDBB49": -91, "": -91, "Telekom-7UNMPx": -92, "Telekom-r6sGoX": -92, "Vodafone-F39B": -93, "Telekom-1F4184": -93, "Telekom-2.4": -95}
{"__location": "Hall", "Pizza": -71, "Telekom-ooMjjf": -76, "c67ace77": -78, "Grogu’s Temple": -78, "STRONG_Bableves": -80, "STRONG_Kifli": -81, "Telekom-Hotspot": -85, "STRONG_Bableves": -86, "STRONG_Kifli": -87, "Telekom-94BCF8": -87, "Telekom-8Dxwfh": -87, "Telekom-iSOTvC": -88, "Telekom-Yeg3O5": -89, "TG": -89, "Telekom-Hotspot": -90, "Vodafone-D76C": -90, "Telekom-687116": -91, "Telekom-1F4184": -91, "Telekom-2.4": -91, "": -91, "Vodafone-F39B": -92, "UPC8EDBB49": -93, "Telekom-7UNMPx": -93, "Telekom-r6sGoX": -93, "Vodafone-7159": -94, "Telekom-Vllhpb": -94}
{"__location": "Hall", "Pizza": -71, "Telekom-ooMjjf": -76, "Grogu’s Temple": -77, "c67ace77": -79, "STRONG_Bableves": -80, "STRONG_Kifli": -80, "Telekom-8Dxwfh": -83, "Telekom-94BCF8": -85, "Telekom-Hotspot": -86, "Telekom-Yeg3O5": -87, "STRONG_Bableves": -88, "Telekom-rQs6gW": -88, "Telekom-iSOTvC": -88, "STRONG_Kifli": -89, "TG": -90, "Telekom-r6sGoX": -90, "Vodafone-D76C": -91, "": -91, "Telekom-687116": -92, "Telekom-2.4": -92, "Vodafone-F39B": -93, "Telekom-Vllhpb": -93, "Telekom-7UNMPx": -94, "UPC7283307": -94}
{"__location": "Hall", "Telekom-ooMjjf": -77, "Pizza": -78, "c67ace77": -79, "STRONG_Kifli": -79, "STRONG_Bableves": -80, "Grogu’s Temple": -83, "Telekom-8Dxwfh": -83, "Telekom-94BCF8": -85, "Telekom-Hotspot": -86, "Telekom-rQs6gW": -86, "Telekom-Yeg3O5": -87, "STRONG_Bableves": -88, "Telekom-iSOTvC": -88, "STRONG_Kifli": -90, "TG": -91, "Telekom-Hotspot": -92, "Telekom-r6sGoX": -92, "Vodafone-D76C": -92, "Telekom-2.4": -92, "": -92, "Telekom-Vllhpb": -93, "Telekom-7UNMPx": -94, "Vodafone-7159": -94, "Vodafone-F39B": -96, "Telekom-1F4184": -96}
{"__location": "Hall", "Telekom-ooMjjf": -73, "Pizza": -76, "Grogu’s Temple": -78, "STRONG_Bableves": -79, "c67ace77": -80, "STRONG_Kifli": -80, "Telekom-Yeg3O5": -84, "Telekom-8Dxwfh": -85, "STRONG_Kifli": -86, "STRONG_Bableves": -87, "Telekom-iSOTvC": -88, "Telekom-94BCF8": -89, "Vodafone-D76C": -89, "Telekom-Hotspot": -90, "Telekom-rQs6gW": -90, "": -90, "Telekom-2.4": -91, "Telekom-r6sGoX": -91, "Telekom-687116": -93, "Vodafone-F39B": -93, "Telekom-1F4184": -94, "UPC7283307": -96}
{"__location": "Hall", "Pizza": -75, "Telekom-ooMjjf": -76, "c67ace77": -77, "STRONG_Bableves": -78, "Grogu’s Temple": -80, "Telekom-8Dxwfh": -83, "STRONG_Bableves": -84, "STRONG_Kifli": -85, "STRONG_Kifli": -86, "Telekom-Hotspot": -88, "Telekom-iSOTvC": -88, "Telekom-94BCF8": -89, "Telekom-Yeg3O5": -89, "Telekom-2.4": -90, "Vodafone-D76C": -91, "": -91, "Vodafone-F39B": -92, "Telekom-687116": -93, "Telekom-1F4184": -93, "Telekom-r6sGoX": -93, "Telekom-Vllhpb": -93, "Telekom-Hotspot": -94, "TG": -95, "UPC7283307": -96}
{"__location": "Hall", "Pizza": -76, "Telekom-ooMjjf": -76, "c67ace77": -77, "Grogu’s Temple": -79, "STRONG_Bableves": -80, "STRONG_Kifli": -82, "Telekom-8Dxwfh": -82, "STRONG_Bableves": -85, "STRONG_Kifli": -86, "Telekom-Hotspot": -87, "Vodafone-D76C": -87, "": -88, "Telekom-94BCF8": -89, "TG": -90, "Telekom-r6sGoX": -90, "Telekom-2.4": -90, "Telekom-Yeg3O5": -91, "Vodafone-F39B": -92, "Telekom-rQs6gW": -95, "UPC7283307": -96}
{"__location": "Hall", "Pizza": -73, "Telekom-ooMjjf": -73, "c67ace77": -77, "Grogu’s Temple": -79, "STRONG_Kifli": -80, "STRONG_Bableves": -81, "STRONG_Bableves": -86, "STRONG_Kifli": -86, "Telekom-8Dxwfh": -88, "Telekom-iSOTvC": -89, "Telekom-r6sGoX": -89, "Telekom-2.4": -90, "Heni": -91, "": -91, "Vodafone-F39B": -92, "TG": -92, "Vodafone-D76C": -92, "Telekom-dcWZu9": -95, "Telekom-Vllhpb": -96, "Telekom-PPcFME": -97}
{"__location": "Hall", "Telekom-ooMjjf": -77, "STRONG_Kifli": -79, "Pizza": -79, "c67ace77": -80, "STRONG_Bableves": -80, "Grogu’s Temple": -80, "Telekom-Yeg3O5": -83, "Telekom-94BCF8": -84, "Telekom-Hotspot": -84, "Telekom-8Dxwfh": -86, "STRONG_Kifli": -88, "STRONG_Bableves": -89, "Telekom-1F4184": -90, "Telekom-Vllhpb": -91, "": -91, "Telekom-rQs6gW": -92, "Telekom-Hotspot": -92, "Telekom-r6sGoX": -92, "Vodafone-D76C": -92, "Vodafone-F39B": -93, "TG": -93, "Heni": -95}
{"__location": "Hall", "Telekom-ooMjjf": -77, "STRONG_Kifli": -79, "c67ace77": -80, "Pizza": -80, "STRONG_Bableves": -81, "Grogu’s Temple": -81, "Telekom-8Dxwfh": -82, "Telekom-Hotspot": -84, "Telekom-94BCF8": -85, "STRONG_Bableves": -86, "Telekom-Yeg3O5": -86, "STRONG_Kifli": -89, "Telekom-Vllhpb": -89, "Telekom-rQs6gW": -90, "Vodafone-D76C": -91, "": -91, "Telekom-7UNMPx": -92, "Telekom-1F4184": -92, "Telekom-Hotspot": -92, "TG": -92, "Telekom-r6sGoX": -92}
{"__location": "Hall", "Telekom-ooMjjf": -76, "STRONG_Bableves": -78, "Pizza": -79, "c67ace77": -81, "STRONG_Kifli": -81, "Grogu’s Temple": -82, "Telekom-Hotspot": -83, "Telekom-94BCF8": -84, "Telekom-Yeg3O5": -84, "Telekom-rQs6gW": -84, "Telekom-8Dxwfh": -85, "STRONG_Kifli": -88, "STRONG_Bableves": -89, "Telekom-1F4184": -91, "Telekom-Hotspot": -91, "Telekom-Vllhpb": -91, "": -91, "Vodafone-F39B": -92, "UPC8EDBB49": -92, "Telekom-7UNMPx": -92, "Telekom-r6sGoX": -92, "Vodafone-D76C": -92, "Telekom-PPcFME": -93, "Heni": -95}
{"__location": "Hall", "Telekom-ooMjjf": -78, "Pizza": -79, "c67ace77": -80, "STRONG_Kifli": -81, "Grogu’s Temple": -81, "STRONG_Bableves": -82, "Telekom-Yeg3O5": -83, "Telekom-8Dxwfh": -83, "Telekom-94BCF8": -84, "Telekom-Hotspot": -85, "Telekom-rQs6gW": -87, "STRONG_Kifli": -88, "STRONG_Bableves": -89, "Telekom-Hotspot": -90, "Telekom-Vllhpb": -90, "Telekom-r6sGoX": -91, "Vodafone-D76C": -91, "Telekom-1F4184": -92, "TG": -92, "Heni": -93, "Telekom-PPcFME": -93, "": -93, "Telekom-7UNMPx": -94, "Telekom-2.4": -94, "Vodafone-F39B": -95}
{"__location": "Hall", "Telekom-ooMjjf": -78, "Grogu’s Temple": -79, "Pizza": -79, "c67ace77": -80, "Telekom-94BCF8": -84, "Telekom-Yeg3O5": -84, "Telekom-8Dxwfh": -84, "STRONG_Bableves": -85, "Telekom-Hotspot": -86, "STRONG_Kifli": -87, "STRONG_Bableves": -89, "STRONG_Kifli": -89, "Telekom-iSOTvC": -90, "UPC8EDBB49": -91, "Telekom-rQs6gW": -91, "Telekom-1F4184": -91, "Telekom-r6sGoX": -91, "": -91, "Vodafone-F39B": -92, "Telekom-Hotspot": -92, "Vodafone-D76C": -92, "Telekom-Vllhpb": -93, "TG": -94}
{"__location": "Hall", "Pizza": -76, "Telekom-ooMjjf": -77, "c67ace77": -81, "Grogu’s Temple": -82, "Telekom-8Dxwfh": -82, "STRONG_Kifli": -83, "STRONG_Bableves": -84, "Telekom-Yeg3O5": -84, "Telekom-Hotspot": -85, "STRONG_Bableves": -89, "STRONG_Kifli": -89, "Telekom-r6sGoX": -89, "Telekom-rQs6gW": -90, "Telekom-1F4184": -90, "Telekom-Hotspot": -91, "TG": -91, "": -91, "Telekom-Vllhpb": -92, "Vodafone-D76C": -92, "Heni": -93, "Vodafone-F39B": -95}
{"__location": "Hall", "Telekom-ooMjjf": -76, "STRONG_Kifli": -80, "Pizza": -80, "c67ace77": -82, "STRONG_Bableves": -82, "Grogu’s Temple": -82, "Telekom-8Dxwfh": -84, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "Telekom-Yeg3O5": -85, "Telekom-1F4184": -87, "STRONG_Bableves": -89, "Telekom-Hotspot": -90, "STRONG_Kifli": -91, "Telekom-r6sGoX": -91, "": -91, "Telekom-Vllhpb": -92, "Telekom-rQs6gW": -93, "Vodafone-F39B": -93, "TG": -94, "Vodafone-D76C": -95}
{"__location": "Hall", "Telekom-ooMjjf": -77, "STRONG_Bableves": -79, "STRONG_Kifli": -79, "c67ace77": -80, "Pizza": -81, "Grogu’s Temple": -82, "Telekom-8Dxwfh": -83, "Telekom-94BCF8": -84, "Telekom-Hotspot": -84, "STRONG_Bableves": -86, "STRONG_Kifli": -86, "Telekom-Yeg3O5": -86, "Telekom-rQs6gW": -89, "Telekom-Hotspot": -91, "TG": -91, "Telekom-r6sGoX": -91, "": -91, "Telekom-7UNMPx": -92, "Telekom-1F4184": -92, "Telekom-Vllhpb": -92, "Vodafone-F39B": -93, "Vodafone-D76C": -93}
{"__location": "Hall", "STRONG_Bableves": -79, "Pizza": -80, "c67ace77": -81, "STRONG_Kifli": -81, "Telekom-8Dxwfh": -81, "Telekom-ooMjjf": -81, "Grogu’s Temple": -83, "Telekom-94BCF8": -85, "Telekom-Hotspot": -86, "Telekom-Yeg3O5": -86, "": -89, "Vodafone-F39B": -90, "STRONG_Kifli": -90, "Telekom-1F4184": -90, "Telekom-Hotspot": -90, "Telekom-Vllhpb": -90, "STRONG_Bableves": -92, "Telekom-rQs6gW": -92, "Telekom-r6sGoX": -92, "TG": -94, "Vodafone-D76C": -95}
{"__location": "Hall", "Telekom-ooMjjf": -77, "c67ace77": -80, "STRONG_Kifli": -81, "Pizza": -82, "STRONG_Bableves": -83, "Grogu’s Temple": -83, "Telekom-8Dxwfh": -83, "Telekom-Yeg3O5": -84, "STRONG_Kifli": -85, "STRONG_Bableves": -86, "Telekom-Hotspot": -86, "Telekom-94BCF8": -87, "": -90, "Telekom-rQs6gW": -91, "Telekom-1F4184": -91, "UPC8EDBB49": -91, "Telekom-Vllhpb": -91, "Vodafone-F39B": -92, "Telekom-Hotspot": -92, "TG": -93, "Telekom-r6sGoX": -93, "T-201722": -94, "Vodafone-D76C": -94, "Telekom-687116": -96}
{"__location": "Hall", "Pizza": -74, "Telekom-8Dxwfh": -81, "Telekom-ooMjjf": -81, "c67ace77": -82, "Grogu’s Temple": -82, "STRONG_Bableves": -82, "STRONG_Kifli": -82, "Telekom-Yeg3O5": -83, "Telekom-94BCF8": -86, "Telekom-Hotspot": -87, "STRONG_Bableves": -88, "STRONG_Kifli": -89, "Telekom-rQs6gW": -89, "Telekom-Vllhpb": -90, "": -90, "TG": -91, "Telekom-r6sGoX": -91, "UPC8EDBB49": -92, "Telekom-687116": -92, "Vodafone-D76C": -93, "Vodafone-F39B": -94, "T-201722": -95, "Heni": -95}
{"__location": "Hall", "Telekom-ooMjjf": -79, "Pizza": -81, "c67ace77": -82, "Grogu’s Temple": -82, "Telekom-8Dxwfh": -82, "STRONG_Bableves": -83, "Telekom-Hotspot": -83, "STRONG_Kifli": -84, "Telekom-94BCF8": -84, "STRONG_Kifli": -85, "Telekom-Yeg3O5": -85, "Telekom-rQs6gW": -89, "Telekom-Hotspot": -89, "": -89, "STRONG_Bableves": -90, "Telekom-1F4184": -90, "Telekom-7UNMPx": -92, "Telekom-r6sGoX": -92, "UPC8EDBB49": -93, "Vodafone-D76C": -93, "Telekom-Vllhpb": -94, "Telekom-2.4": -94, "Vodafone-F39B": -95}
{"__location": "Hall", "Telekom-8Dxwfh": -79, "Telekom-ooMjjf": -79, "STRONG_Bableves": -81, "c67ace77": -82, "Pizza": -83, "STRONG_Kifli": -84, "Telekom-94BCF8": -84, "Telekom-Hotspot": -84, "Telekom-Yeg3O5": -84, "STRONG_Bableves": -85, "Grogu’s Temple": -85, "STRONG_Kifli": -86, "": -89, "Telekom-1F4184": -90, "Telekom-r6sGoX": -90, "Telekom-Vllhpb": -91, "UPC8EDBB49": -92, "Vodafone-F39B": -92, "Telekom-Hotspot": -92, "Vodafone-D76C": -92, "TG": -94}
{"__location": "Hall", "c67ace77": -80, "Telekom-ooMjjf": -81, "Pizza": -82, "Telekom-8Dxwfh": -82, "STRONG_Bableves": -83, "Grogu’s Temple": -83, "STRONG_Kifli": -84, "Telekom-Yeg3O5": -85, "Telekom-94BCF8": -86, "Telekom-Hotspot": -86, "STRONG_Bableves": -87, "STRONG_Kifli": -88, "Telekom-Vllhpb": -89, "": -89, "Telekom-rQs6gW": -91, "Telekom-r6sGoX": -91, "Vodafone-F39B": -92, "Vodafone-D76C": -92, "UPC8EDBB49": -93, "Telekom-1F4184": -93, "Telekom-7UNMPx": -93}
{"__location": "Hall", "Pizza": -75, "Telekom-ooMjjf": -75, "c67ace77": -82, "STRONG_Kifli": -82, "STRONG_Bableves": -82, "Telekom-8Dxwfh": -82, "Grogu’s Temple": -83, "Telekom-Yeg3O5": -85, "STRONG_Kifli": -86, "Telekom-Hotspot": -86, "Telekom-iSOTvC": -86, "Telekom-94BCF8": -87, "STRONG_Bableves": -88, "Telekom-r6sGoX": -89, "Telekom-rQs6gW": -90, "Telekom-Vllhpb": -90, "": -90, "UPC8EDBB49": -91, "Telekom-1F4184": -92, "Telekom-7UNMPx": -92, "Vodafone-D76C": -92, "Vodafone-F39B": -93, "Telekom-Hotspot": -93}
{"__location": "Hall", "Pizza": -74, "Telekom-ooMjjf": -81, "c67ace77": -82, "Telekom-8Dxwfh": -82, "STRONG_Bableves": -84, "STRONG_Kifli": -84, "Grogu’s Temple": -84, "Telekom-Yeg3O5": -85, "Telekom-iSOTvC": -85, "STRONG_Kifli": -87, "Telekom-Hotspot": -88, "STRONG_Bableves": -89, "Telekom-rQs6gW": -89, "": -89, "Telekom-r6sGoX": -91, "Vodafone-D76C": -91, "UPC8EDBB49": -92, "Telekom-Vllhpb": -93, "Heni": -94, "Vodafone-F39B": -95}
{"__location": "Hall", "Pizza": -74, "Telekom-ooMjjf": -80, "c67ace77": -82, "STRONG_Kifli": -82, "STRONG_Bableves": -83, "STRONG_Bableves": -83, "Telekom-8Dxwfh": -83, "Grogu’s Temple": -84, "Telekom-94BCF8": -85, "Telekom-Yeg3O5": -85, "STRONG_Kifli": -86, "Telekom-Hotspot": -86, "Telekom-iSOTvC": -86, "Telekom-rQs6gW": -90, "Telekom-r6sGoX": -91, "UPC8EDBB49": -92, "": -92, "Vodafone-F39B": -93, "Telekom-1F4184": -93, "Telekom-Hotspot": -93, "Telekom-Vllhpb": -93, "Vodafone-D76C": -94, "Telekom-7UNMPx": -95}
{"__location": "Hall", "Telekom-ooMjjf": -79, "Pizza": -81, "Telekom-8Dxwfh": -81, "c67ace77": -82, "Grogu’s Temple": -83, "STRONG_Kifli": -83, "STRONG_Bableves": -84, "STRONG_Kifli": -84, "Telekom-Yeg3O5": -84, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "Telekom-iSOTvC": -86, "STRONG_Bableves": -88, "Telekom-rQs6gW": -90, "Telekom-Vllhpb": -90, "Vodafone-F39B": -91, "Telekom-1F4184": -91, "Telekom-r6sGoX": -91, "Vodafone-D76C": -91, "": -91, "Telekom-Hotspot": -92, "UPC8EDBB49": -93}
{"__location": "Hall", "Telekom-ooMjjf": -80, "c67ace77": -81, "Telekom-8Dxwfh": -81, "Pizza": -82, "Grogu’s Temple": -84, "STRONG_Bableves": -84, "Telekom-iSOTvC": -84, "STRONG_Kifli": -85, "Telekom-94BCF8": -85, "STRONG_Kifli": -86, "Telekom-Yeg3O5": -86, "STRONG_Bableves": -87, "Vodafone-D76C": -90, "Telekom-r6sGoX": -91, "Telekom-Vllhpb": -91, "": -91, "UPC8EDBB49": -92, "Vodafone-F39B": -94, "TG": -94}
{"__location": "Hall", "Telekom-ooMjjf": -74, "STRONG_Bableves": -79, "STRONG_Kifli": -79, "Telekom-iSOTvC": -79, "c67ace77": -80, "Telekom-Yeg3O5": -80, "Grogu’s Temple": -82, "Telekom-94BCF8": -82, "Telekom-Hotspot": -82, "Pizza": -82, "Telekom-8Dxwfh": -85, "Telekom-r6sGoX": -89, "Telekom-Vllhpb": -90, "STRONG_Kifli": -91, "Heni": -91, "Telekom-rQs6gW": -91, "T-965259": -92, "Telekom-2.4": -92, "Telekom-687116": -93, "Telekom-PPcFME": -93, "": -93, "STRONG_Bableves": -94, "1e1f82c3": -94, "Vodafone-D76C": -94}
{"__location": "Hall", "Grogu’s Temple": -74, "Telekom-Yeg3O5": -76, "c67ace77": -78, "Telekom-ooMjjf": -78, "Pizza": -79, "Telekom-8Dxwfh": -82, "Telekom-94BCF8": -84, "Telekom-iSOTvC": -84, "Telekom-Hotspot": -85, "STRONG_Kifli": -88, "STRONG_Bableves": -88, "STRONG_Bableves": -89, "STRONG_Kifli": -89, "TG": -89, "Telekom-2.4": -89, "Telekom-Vllhpb": -89, "Heni": -90, "Vodafone-D76C": -90, "": -90, "Telekom-rQs6gW": -91, "Telekom-dcWZu9": -91, "UPC7283307": -92, "UPC2355650": -93, "Vodafone-F39B": -93, "Telekom-r6sGoX": -93, "UPC8EDBB49": -94, "1e1f82c3": -94, "T-201722": -95}
{"__location": "Living Room", "Pizza": -70, "STRONG_Kifli": -72, "STRONG_Bableves": -73, "Telekom-ooMjjf": -73, "Grogu’s Temple": -80, "Telekom-94BCF8": -85, "Telekom-Hotspot": -85, "Telekom-iSOTvC": -85, "Telekom-Yeg3O5": -86, "Telekom-8Dxwfh": -88, "STRONG_Bableves": -90, "Vodafone-D76C": -90, "STRONG_Kifli": -92, "Telekom-dcWZu9": -92, "Liliom": -92, "c67ace77": -93, "UPC8EDBB49": -93, "Vodafone-7159": -93, "Telekom-474071": -94, "Telekom-2.4": -94}
{"__location": "Living Room", "Pizza": -71, "Telekom-ooMjjf": -73, "Grogu’s Temple": -78, "Telekom-Yeg3O5": -79, "STRONG_Kifli": -82, "STRONG_Bableves": -83, "Telekom-94BCF8": -84, "Telekom-Hotspot": -84, "Telekom-iSOTvC": -85, "Telekom-8Dxwfh": -86, "Vodafone-D76C": -89, "Liliom": -90, "Telekom-rQs6gW": -91, "Telekom-Vllhpb": -91, "": -91, "Telekom-474071": -92, "STRONG_Bableves": -92, "Telekom-r6sGoX": -93, "Telekom-dcWZu9": -94, "STRONG_Kifli": -94, "Telekom-2.4": -94, "c67ace77": -95, "TG": -97}
{"__location": "Living Room", "Pizza": -71, "STRONG_Kifli": -72, "STRONG_Bableves": -72, "Telekom-ooMjjf": -74, "Telekom-Yeg3O5": -78, "Grogu’s Temple": -79, "Telekom-8Dxwfh": -84, "Telekom-Hotspot": -85, "Telekom-94BCF8": -86, "Telekom-iSOTvC": -86, "STRONG_Bableves": -86, "STRONG_Kifli": -87, "Vodafone-D76C": -88, "Telekom-dcWZu9": -92, "Telekom-474071": -92, "Telekom-r6sGoX": -92, "c67ace77": -93, "Telekom-rQs6gW": -93, "Liliom": -93, "Telekom-2.4": -93, "": -93, "Telekom-Vllhpb": -94, "TG": -97}
{"__location": "Living Room", "STRONG_Kifli": -69, "STRONG_Bableves": -71, "Telekom-ooMjjf": -73, "Pizza": -76, "Grogu’s Temple": -79, "Telekom-Hotspot": -84, "Telekom-iSOTvC": -84, "Telekom-8Dxwfh": -85, "STRONG_Bableves": -86, "Telekom-94BCF8": -86, "Telekom-Yeg3O5": -86, "STRONG_Kifli": -87, "Vodafone-D76C": -88, "": -91, "Liliom": -92, "Telekom-r6sGoX": -92, "Telekom-dcWZu9": -93, "UPC8EDBB49": -93, "Telekom-rQs6gW": -93, "c67ace77": -94, "Telekom-474071": -94, "Telekom-Hotspot": -94, "Telekom-1F4184": -95}
{"__location": "Living Room", "Telekom-ooMjjf": -71, "STRONG_Kifli": -72, "STRONG_Bableves": -73, "Pizza": -76, "Grogu’s Temple": -80, "Telekom-94BCF8": -84, "Telekom-Hotspot": -85, "Telekom-iSOTvC": -85, "Vodafone-D76C": -88, "Telekom-Yeg3O5": -88, "Telekom-r6sGoX": -90, "Telekom-Vllhpb": -90, "Telekom-rQs6gW": -91, "Telekom-8Dxwfh": -91, "Liliom": -91, "c67ace77": -92, "Telekom-dcWZu9": -92, "Telekom-474071": -93, "UPC8EDBB49": -94, "Telekom-1F4184": -94, "TG": -94, "Telekom-Hotspot": -96}
{"__location": "Living Room", "Telekom-ooMjjf": -70, "Pizza": -71, "STRONG_Bableves": -72, "STRONG_Kifli": -74, "Grogu’s Temple": -79, "Telekom-94BCF8": -83, "Telekom-Hotspot": -83, "Telekom-iSOTvC": -86, "Telekom-Yeg3O5": -86, "Telekom-8Dxwfh": -87, "STRONG_Bableves": -88, "STRONG_Kifli": -88, "Vodafone-D76C": -90, "Liliom": -91, "Telekom-dcWZu9": -92, "UPC8EDBB49": -92, "Telekom-rQs6gW": -92, "Telekom-r6sGoX": -92, "Telekom-474071": -94, "Telekom-Vllhpb": -94, "": -94, "c67ace77": -95}
{"__location": "Living Room", "Pizza": -70, "Telekom-ooMjjf": -74, "Grogu’s Temple": -82, "STRONG_Kifli": -83, "STRONG_Bableves": -84, "Telekom-94BCF8": -84, "Telekom-8Dxwfh": -84, "Telekom-Hotspot": -85, "Telekom-iSOTvC": -85, "Vodafone-D76C": -87, "Telekom-Yeg3O5": -87, "": -90, "Telekom-r6sGoX": -92, "Liliom": -92, "Vodafone-F39B": -92, "Telekom-Hotspot": -93, "dlink_121": -93, "TG": -93, "Telekom-dcWZu9": -94, "Telekom-rQs6gW": -94, "Telekom-1F4184": -94, "Telekom-Vllhpb": -94, "c67ace77": -95, "Telekom-474071": -96, "UPC8EDBB49": -96, "STRONG_Bableves": -96}
{"__location": "Living Room", "Pizza": -72, "Grogu’s Temple": -78, "STRONG_Kifli": -80, "STRONG_Bableves": -81, "Telekom-8Dxwfh": -81, "Telekom-94BCF8": -82, "Telekom-Hotspot": -82, "Vodafone-D76C": -84, "c67ace77": -87, "Telekom-Yeg3O5": -88, "UPC8EDBB49": -90, "Telekom-ooMjjf": -90, "Telekom-474071": -91, "Vodafone-F39B": -93, "T-201722": -93, "Heni": -93, "TG": -93, "STRONG_Bableves": -94, "STRONG_Kifli": -94, "Telekom-iSOTvC": -94, "Telekom-Hotspot": -94, "Telekom-PPcFME": -94, "Telekom-1F4184": -95, "Telekom-2.4": -95}
{"__location": "Living Room", "Pizza": -71, "Telekom-94BCF8": -76, "Telekom-Hotspot": -76, "Grogu’s Temple": -78, "Telekom-8Dxwfh": -79, "Vodafone-D76C": -81, "STRONG_Bableves": -82, "STRONG_Kifli": -82, "Telekom-iSOTvC": -83, "Telekom-Yeg3O5": -88, "Telekom-474071": -89, "STRONG_Bableves": -90, "STRONG_Kifli": -90, "c67ace77": -91, "UPC8EDBB49": -91, "Heni": -91, "TG": -92, "Telekom-Vllhpb": -94, "Telekom-2.4": -96}
{"__location": "Living Room", "Pizza": -71, "Telekom-94BCF8": -77, "Telekom-Hotspot": -77, "STRONG_Kifli": -78, "Telekom-8Dxwfh": -80, "Telekom-iSOTvC": -82, "STRONG_Bableves": -83, "Vodafone-D76C": -85, "Telekom-474071": -88, "Grogu’s Temple": -88, "STRONG_Kifli": -89, "STRONG_Bableves": -90, "c67ace77": -90, "Telekom-Yeg3O5": -91, "Telekom-Vllhpb": -93, "UPC8EDBB49": -94, "Heni": -94, "Telekom-2.4": -95}
{"__location": "Living Room", "Pizza": -71, "Telekom-94BCF8": -77, "Telekom-Hotspot": -77, "Telekom-8Dxwfh": -80, "STRONG_Bableves": -83, "STRONG_Kifli": -83, "Telekom-iSOTvC": -83, "Vodafone-D76C": -84, "Grogu’s Temple": -87, "Telekom-474071": -90, "Telekom-Yeg3O5": -90, "STRONG_Bableves": -91, "c67ace77": -92, "UPC8EDBB49": -92, "T-201722": -92, "Heni": -92, "STRONG_Kifli": -93, "Telekom-ooMjjf": -94, "": -95, "Telekom-2.4": -97}
{"__location": "Living Room", "Telekom-Hotspot": -76, "STRONG_Kifli": -77, "Telekom-94BCF8": -77, "STRONG_Bableves": -78, "Telekom-8Dxwfh": -80, "Telekom-iSOTvC": -81, "Vodafone-D76C": -81, "Pizza": -82, "Grogu’s Temple": -87, "STRONG_Kifli": -89, "Telekom-Yeg3O5": -89, "c67ace77": -90, "STRONG_Bableves": -90, "Telekom-ooMjjf": -90, "Telekom-474071": -91, "Heni": -91, "": -92, "UPC8EDBB49": -93, "Telekom-2.4": -93, "TG": -94}
{"__location": "Living Room", "STRONG_Kifli": -77, "Telekom-94BCF8": -77, "Telekom-Hotspot": -78, "Telekom-iSOTvC": -78, "Grogu’s Temple": -79, "Pizza": -80, "STRONG_Bableves": -81, "Telekom-8Dxwfh": -81, "Vodafone-D76C": -83, "STRONG_Kifli": -88, "c67ace77": -89, "Telekom-Yeg3O5": -89, "Telekom-ooMjjf": -90, "Telekom-474071": -91, "STRONG_Bableves": -91, "Telekom-2.4": -93, "": -93, "Heni": -94, "Telekom-rQs6gW": -94, "UPC8EDBB49": -97}
{"__location": "Living Room", "Pizza": -75, "STRONG_Bableves": -78, "STRONG_Kifli": -79, "Telekom-8Dxwfh": -79, "Telekom-94BCF8": -80, "Telekom-ooMjjf": -80, "Telekom-Hotspot": -81, "Grogu’s Temple": -82, "Telekom-Yeg3O5": -86, "c67ace77": -88, "Telekom-iSOTvC": -88, "STRONG_Bableves": -89, "Telekom-474071": -90, "STRONG_Kifli": -91, "TG": -91, "Vodafone-D76C": -91, "Telekom-Vllhpb": -91, "dlink_121": -92, "Telekom-7UNMPx": -92, "Telekom-2.4": -92, "": -92, "UPC8EDBB49": -93, "Heni": -93, "Telekom-Hotspot": -93, "Telekom-dcWZu9": -93, "Vodafone-7159": -93, "Telekom-1F4184": -95, "Telekom-r6sGoX": -95, "1e1f82c3": -97}
    '''
    X, y, classmap, converter_code = port_wifi_indoor_positioning(samples)
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    print(port(clf, classmap=classmap))
    with open("Classifier.h", "w") as f:
        print(port(clf, classmap=classmap), file=f)