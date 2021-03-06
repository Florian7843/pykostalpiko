<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">pykostalpiko</h3>

  <p align="center">
    A simple python library to interface with a Kostal Piko Solar inverter
    <br />
    <a href="https://github.com/Florian7843/pykostalpiko"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Florian7843/pykostalpiko/issues">Report Bug</a>
    ·
    <a href="https://github.com/Florian7843/pykostalpiko/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project aims to support the same functionallity as the web interface of the Piko inverter and provide a friendly way to access it using python.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Installation
```sh
pip install pykostalpiko
```

### Examples

#### Print the current values of the inverter
```python
import asyncio

from aiohttp import ClientSession

from pykostalpiko import Piko
from pykostalpiko.dxs.current_values import LIST

async def asnyc_main():
    async with ClientSession() as session:
        async with Piko(session, "<ip-address>") as piko:
            print(await piko.async_fetch_multiple(LIST))


asyncio.run(asnyc_main())
```

#### Change the name of the inverter
```python
import asyncio

from aiohttp import ClientSession

from pykostalpiko import Piko
from pykostalpiko.dxs.inverter import NAME

async def asnyc_main():
    async with ClientSession() as session:
        async with Piko(session, "<ip-address>", "username", "password") as piko:
            await piko.async_set_descriptors([(NAME, "<new-name>")])

asyncio.run(asnyc_main())
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Florian Schmidt - floriansch7843@gmail.com

Project Link: [https://github.com/Florian7843/pykostalpiko](https://github.com/Florian7843/pykostalpiko)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [pykostal](https://github.com/DAMEK86/pykostal)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Florian7843/pykostalpiko.svg?style=for-the-badge
[contributors-url]: https://github.com/Florian7843/pykostalpiko/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Florian7843/pykostalpiko.svg?style=for-the-badge
[forks-url]: https://github.com/Florian7843/pykostalpiko/network/members
[stars-shield]: https://img.shields.io/github/stars/Florian7843/pykostalpiko.svg?style=for-the-badge
[stars-url]: https://github.com/Florian7843/pykostalpiko/stargazers
[issues-shield]: https://img.shields.io/github/issues/Florian7843/pykostalpiko.svg?style=for-the-badge
[issues-url]: https://github.com/Florian7843/pykostalpiko/issues
[license-shield]: https://img.shields.io/github/license/Florian7843/pykostalpiko.svg?style=for-the-badge
[license-url]: https://github.com/Florian7843/pykostalpiko/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
