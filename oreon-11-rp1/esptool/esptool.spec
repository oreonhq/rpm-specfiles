%global source0_hash 0ff7bdc531d1f10caeffa90ff74383f80bf952b74db73171d66cd445ff40aa5f
Name:           esptool
Version:        5.4.0
Release:        1%{?dist}
Summary:        A utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32
License:        GPL-2.0-or-later
URL:            https://github.com/espressif/%{name}
Source0:        https://github.com/espressif/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       %{name}.py = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-esptool = %{version}-%{release}
# /oreon:deps
%package -n       python3-esptool+dev
Summary:        Metapackage for python3-esptool dev extras
Requires:       python3-esptool = %{version}-%{release}
Requires:       python3dist(coverage) >= 6.0
Provides:       python3dist(esptool[dev]) = %{version}-%{release}

%description -n python3-esptool+dev
Metapackage for python3-esptool dev extras.

%package -n       python3-esptool+hsm
Summary:        Metapackage for python3-esptool hsm extras
Requires:       python3-esptool = %{version}-%{release}
Provides:       python3dist(esptool[hsm]) = %{version}-%{release}

%description -n python3-esptool+hsm
Metapackage for python3-esptool hsm extras.

%package -n       python3-esptool+docs
Summary:        Metapackage for python3-esptool docs extras
Requires:       python3-esptool = %{version}-%{release}
Requires:       python3dist(esp-docs) >= 2.1.4
Requires:       python3dist(esp-docs) < 3
Provides:       python3dist(esptool[docs]) = %{version}-%{release}

%description -n python3-esptool+docs
Metapackage for python3-esptool docs extras.

%description
%{name}.py A command line utility to communicate with the ROM bootloader in
Espressif ESP8266 & ESP32 WiFi microcontroller. Allows flashing firmware,
reading back firmware, querying chip parameters, etc.
Developed by the community, not by Espressif Systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import -e 'espsecure.esp_hsm_sign*'
%pytest -m host_test --ignore test/test_espsecure_hsm.py -k "not ecdsa192"
%files

%changelog

%autochangelog
