%global source0_hash 74067faf6837f18af7acf6e61e0b9a4c0851bcc58a06ea846b14e5f30c000ecd

Name:           esptool
Version:        5.2.0
Release:        %autorelease
Summary:        A utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32

License:        GPL-2.0-or-later
URL:            https://github.com/espressif/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-rerunfailures
BuildRequires:  python3-pyelftools
BuildRequires:  python3-requests

Provides:       %{name}.py = %{version}-%{release}

%description
%{name}.py A command line utility to communicate with the ROM bootloader in
Espressif ESP8266 & ESP32 WiFi microcontroller. Allows flashing firmware,
reading back firmware, querying chip parameters, etc.
Developed by the community, not by Espressif Systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files esptool espefuse espsecure esp_rfc2217_server

%check
# There is esptool[hsm] which pulls additional requirement on python-pkcs11
# It is not yet packaged in Fedora though
# ecdsa192 is unsupported in Fedora, skip tests using it
%pyproject_check_import -e 'espsecure.esp_hsm_sign*'
%pytest -m host_test --ignore test/test_espsecure_hsm.py -k "not ecdsa192"

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{_bindir}/espefuse
%{_bindir}/espefuse.py
%{_bindir}/espsecure
%{_bindir}/espsecure.py
%{_bindir}/esp_rfc2217_server
%{_bindir}/esp_rfc2217_server.py

%changelog
%autochangelog
