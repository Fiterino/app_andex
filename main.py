from mapapi_PG import show_map


def main():
    ll, span = '43.141580551356746,51.5570779896406', '0.001,0.001'
    show_map(f'll={ll}&spn={span}')


if __name__ == '__main__':
    main()