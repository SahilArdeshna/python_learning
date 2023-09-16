import sys
import hashlib
import requests


def request_api_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetchin: {res.status_code}, check the api and try again"
        )

    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count

    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]

    response = request_api_data(first5_char)
    return get_password_leaks_count(response.text, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(
                f"{password} was found {count} times... you should change probably change your password!"
            )
        else:
            print(f"{password} was not found. Carry on!")

    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
