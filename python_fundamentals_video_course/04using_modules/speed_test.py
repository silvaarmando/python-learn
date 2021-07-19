import speedtest

s = speedtest.Speedtest()

print('Testing... \n')

download_speed = s.download() / 1048576
upload_speed = s.upload() / 1048576
ping_result = round(s.results.ping)

print(f'Download speed: {dowload_speed:.2f} Mbps')
print(f'Download speed: {dowload_speed:.2f} Mbps')
print(f'Ping: {ping_result} ms')
