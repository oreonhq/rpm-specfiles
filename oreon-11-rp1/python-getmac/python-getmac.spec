%global source0_hash 456435cdbf1f5f45c433a250b8b795146e893b6fc659060f15451e812a2ab17d

%global srcname getmac

Name:           python-%{srcname}
Version:        0.9.5
Release:        7%{?dist}
Summary:        Python module to get the MAC address of local network interfaces and LAN hosts

License:        MIT
URL:            https://github.com/GhostofGoes/getmac
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools

%description
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-getmac}

%description -n python3-%{srcname}
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
sed -i '1{/^#!\//d}' getmac/__main__.py
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
/usr/bin/getmac

%changelog
%autochangelog
