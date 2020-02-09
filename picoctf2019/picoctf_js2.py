from selenium import webdriver
import HHCTF.util as hu

raw = "Ehk3/Pjm+PZ8K43TSc2iuxDfAI5JA07jkUGOfwAyH7Z7O07EDf0aPzpCYHSaNRPnpskBwQBFAUQmAACsOAD+eCpqAGCTCkQKXQAADWFIv//jH0aAxgBaciJ4nIJAwN4A442cJ/RJGkGuB+gNeE3JUgAADd5Qhmk6AIODAEU3AGyJUBUAfgEJ7AHUo+2bO0TkAAC8R/MBTBFUjTej5ihfM6QA+HJ8fFUHMMyAZvvjijMwDNsCq4j4a2Wayvg+bphkzc2+nyZU/tXsMiLeQv31Nww1AqMVx2id48bvzCJVlq+J8m/pkSKIaN9/N0VWh41W/l/AWwvk1T0MQAE07/+2ZqrfyHQ8/C7f+f9fw1HpnoABXH4nI+R89D09nR/dImTqFSg/HVZQRCrGLJNiyI+9u6sshf1oNDVKoGaA/N9/chOu/6oSJ/zCVRs/sT4QzaE7eqUp/KF6of0zm39DLqYiPUDxgm2Ea1ENe87JUHx38SHxLQhcxpEHuyXEVFbTs3uq/cb1b5YPrMrGV9FPMTJOatQBrbG3f8ev72P85iwqtu1oClqOOWkRjvZl373rz/8VBsDuVxod11sk3UdUv/PxgfwVCq2h1Ci6mhS0XhN+Cgj66v0ihSpNqNSCwucpfjKwJqCoPWJM/TjOT2zrzEOv/v07u6+UX9O/wyuLPcO1q8mIR/QJ/3b8/NXLW/Iu8hdWJn/26yx+kjAVNRWcrK5Pv4/8MRGiPeQ48T3G3zmAWj8V3x9X221V422GOEUh39eKmoE6KNnLE6qh3F2PqTajxVl8oxUBmJ/MZnJr79k20r+kQ7ML6rd89EggfAT3i8xzI/LtGCOUGCgwnts8bzicdwICPSm05F3Zq/84XXWmn3NmvrVPNvVTv6+UHngvC1/WZv5jvWN6a6YFylfePuXf0/Ld1z+ZnMu2BlSsP7L8lSLpeOcxr7OTJw9qZeMAStb9"
raw = hu.from_base64(raw)

matches = [
    0x89, 0x50, 0x4E, 0x47,
    0x0D, 0x0A, 0x1A, 0x0A,
    0x00, 0x00, 0x00, 0x0d,
    0x49, 0x48, 0x44, 0x52
]

candicates = [
    [], [], [], [],
    [], [], [], [],
    [], [], [], [],
    [], [], [], []
]


for idx in range(0, len(raw)):
    if idx % 16 == 0:
        print('{:2d} |'.format(idx // 16), end='')
    print(' ' + hu.to_hex(raw[idx]), end='')
    if matches[idx % 16] == raw[idx]:
        candicates[idx % 16].append(idx // 16)
    if idx % 16 == 15:
        print('')

for idx in range(0, 16):
    print('{:2d} |'.format(idx), end='')
    for cand in candicates[idx]:
        print(f' {cand}', end='')
    print('')








options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


def save(input):
    print(input)
    driver.get('https://2019shell1.picoctf.com/problem/32262/?#')
    search_box = driver.find_element_by_id("user_in")
    search_box.clear()
    search_box.send_keys(input)
    search_box.submit()
    driver.save_screenshot(input + '.png')

def dfs(cu, query):
    global candicates
    
    if cu == 16:
        save(query)
        return
    
    for digit in candicates[cu]:
        if digit < 10:
            dfs(cu + 1, query + str(digit) + '0')

dfs(0, '')

driver.quit()
