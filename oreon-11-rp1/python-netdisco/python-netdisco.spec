%global source0_hash 8cd2b480103c2dee9ee6792490f2770875ea5076167a26b90444f96d8c07523c

%global srcname netdisco

Name:           python-netdisco
Version:        3.0.0
Release:        17%{?dist}
Summary:        Python library to scan local network for services and devices

License:        MIT
URL:            https://github.com/home-assistant/netdisco
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# Untracked dependancy
BuildRequires:  python3dist(pytest)

%description
NetDisco is a Python 3 library to discover local devices and services. It
allows to scan on demand or offer a service that will scan the network in
the background in a set interval.

Current methods of scanning:
- mDNS (includes Chromecast, Homekit)
- uPnP
- Plex Media Server using Good Day Mate protocol
- Logitech Media Server discovery protocol
- Daikin discovery protocol
- Web OS discovery protocol

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-zeroconf
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{srcname}
NetDisco is a Python 3 library to discover local devices and services. It
allows to scan on demand or offer a service that will scan the network in
the background in a set interval.

Current methods of scanning:
- mDNS (includes Chromecast, Homekit)
- uPnP
- Plex Media Server using Good Day Mate protocol
- Logitech Media Server discovery protocol
- Daikin discovery protocol
- Web OS discovery protocol

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -v tests --ignore "tests/test_xboxone.py"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
