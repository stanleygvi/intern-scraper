import requests
import json
import pandas as pd
cookies = {
    '_vwo_uuid': 'J43B69C0154E4CBE9242D61522F461449',
    '_vwo_ds': '3%241683327076%3A85.25953135%3A%3A',
    '_vwo_uuid_v2': 'DFA294E6EF95BB4C9064957ED15C34EA9|aea8aa10014c0024f91575f7cbb43d72',
    '_gcl_au': '1.1.309554034.1683327078',
    '_uetsid': '58b2eb20eb9711ed8d799b9d16cc708e',
    '_uetvid': '58b35ba0eb9711edab630db449f08c94',
    'ln_or': 'eyIzNzYwNzg1IjoiZCJ9',
    '_gid': 'GA1.2.388479833.1683327078',
    '__qca': 'P0-2093164207-1683327078120',
    'OptanonAlertBoxClosed': '2023-05-05T22:51:20.662Z',
    '__cf_bm': 'bZ3MulXEpyfupChFlZGYNBjcJtutf3tgAgpugv0tbZ4-1683332527-0-AcaslFgUfbUxX9fa2Vq09YU5KqLUxrEvbnK2imk8ritWajNZxflMNSFA6I+RWRZUpeQrCiC9Q8hrgCWd9lGSNEk=',
    '_vis_opt_s': '2%7C',
    '_vis_opt_test_cookie': '1',
    '_gac_UA-100612346-2': '1.1683332531.Cj0KCQjw0tKiBhC6ARIsAAOXutkf87UzTbqqCCcaRNXXJb_DNuoTJh6FbQivMXrmklAlmSm5BhOL7KQaAhPQEALw_wcB',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+May+05+2023+17%3A22%3A12+GMT-0700+(Pacific+Daylight+Time)&version=202302.1.0&isIABGlobal=false&hosts=&consentId=4b5fe9b8-16ab-4ffd-809e-29ef9205352f&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2CC0003%3A1%2C2%3A1%2C4%3A0%2CSSPD_BG%3A0%2CC007%3A0%2CC008%3A0&geolocation=US%3BCA&AwaitingReconsent=false',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.roberthalf.com%2Fhire%3Futm_source%3Dgoogle%26utm_medium%3Dppc%26utm_term%3Drobert%2520half%26matchtype%3De%26utm_campaign%3DRobert-Half-Google-Brand%26customer_id%3D716-943-9551%26specialized_service_dropdown%3D%26campaignName%3DRobert%2BHalf%2B-%2BGoogle%2B-%2BBrand%26position_hiring%3D%26request_type_dropdown%3D%26mkwid%3Dl9PyBtBH-dc_pcrid_568494722303_pkw_robert%2520half_pmt_e_pdv_c_pgrid_127838497581_ptaid_kwd-40197400_%26traffic%3Dps%26intent%3D%26callcamp%3Dnational_paid_search%26gad%3D1%26gclid%3DCj0KCQjw0tKiBhC6ARIsAAOXutkf87UzTbqqCCcaRNXXJb_DNuoTJh6FbQivMXrmklAlmSm5BhOL7KQaAhPQEALw_wcB~1683332530372%7Chttps%3A%2F%2Fwww.roberthalf.com%2Fjobs~1683332532397',
    'fs_lua': '1.1683332532401',
    'fs_uid': '#14XMWD#ddb99397-cd85-4ba8-8279-8320a8b0ac8a:73d518c4-cf45-4742-b417-b75108d4b539:1683327078286::13#/1714863078',
    '_ga': 'GA1.1.1461347345.1683327078',
    'invoca_session': '%7B%22ttl%22%3A%222023-05-20T00%3A22%3A16.436Z%22%2C%22session%22%3A%7B%22invoca_id%22%3A%22i-df2226e5-2372-4e8d-aaca-b51e0e49bd96%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22rn%22%3Afalse%7D%7D',
    '_vwo_sn': '5452%3A3',
    'utag_main': 'v_id:0187ee1ccbf90005b323ca40eebb05075004606d00942$_sn:2$_se:15$_ss:0$_st:1683334361473$dc_visit:2$ses_id:1683330259401%3Bexp-session$_pn:9%3Bexp-session$dc_event:15%3Bexp-session$dc_region:eu-central-1%3Bexp-session$ga_cid:1461347345.1683327078%3Bexp-session',
    '_ga_N8XPZB97KF': 'GS1.1.1683330259401.1.1.1683332561.0.0.0',
}

HEADERS = {
    'authority': 'www.roberthalf.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.roberthalf.com/jobs/software-engineer/94706',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
def send_request(keywords, zip_code):
    params = {
        'keywords': keywords,
        'location': zip_code,
        'page': '0',
    }
    # Robert Half sends parameters to ajax to recieve data
    response = requests.get('https://www.roberthalf.com/ajax/job-results/', params=params, cookies=cookies, headers=HEADERS)
    response_json = json.loads(response.content)
    return response_json

def format_job(job):
    job_dict = {
        "title":[job['title']],
        "job_type":[job['jobType']],
        "salary":[job['salary'].split("/")[0]],
        "payPeriod":[job['payPeriod']],
        "city":[job['city']],
        "isRemote":str([job['isRemote']]),
        "link":[job['absoluteUrl']],
        "applyLink":["https://www.roberthalf.com/" + job['applyUrl']],
        "employeeType":[job['empType']],
    }
    job_df = pd.DataFrame(job_dict)
    return job_df

def parse_response(response_json):
    jobs = response_json['jobs']
    jobs_df = pd.DataFrame({
        "title":[],
        "job_type":[],
        "salary":[],
        "payPeriod":[],
        "city":[],
        "isRemote":[],
        "link":[],
        "applyLink":[],
        "employeeType":[],
    })
    for job in jobs:
        job_df = format_job(job)
        jobs_df = jobs_df.append(job_df, ignore_index = True)
    return jobs_df

def write_to_csv(df, outfile):
    df.to_csv(f'{outfile}.csv') 
           

def scrape_rf(keywords,zip_code ):
    response_json = send_request(keywords, zip_code)
    response_df = parse_response(response_json)
    write_to_csv(response_df,'robert_half')
    return response_df


if __name__ == '__main__':
    df = scrape_rf('programmer', '94706')
    print(df)
    # write_to_csv(df, 'robert_half')