%global source0_hash 624e7cb171e093b96efa19ec9ce0678631906eff3bf65e3f0e445eccb7c44ffa
%global _hardened_build 1
Name:           onionshare
Version:        2.6.5
Release:        1%{?dist}
Summary:        Securely and anonymously share files of any size
License:        GPL-3.0-only
URL:            https://onionshare.org/
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-flask
Requires:       python3-stem
Requires:       python3-qt5
Requires:       nautilus-python
Requires:       tor
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
OnionShare lets you securely and anonymously share files of any size. It works
by starting a web server, making it accessible as a Tor hidden service, and
generating an unguessable URL to access and download files. It doesn't require
setting up a server on the internet somewhere or using a third party
file sharing service. You host files on your own computer and use a Tor
hidden service to make it temporarily accessible over the internet. The other
user just needs to use Tor Browser to download a file from you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}

#%patch0 -p1 -b .orig

%build

(cd cli; %{__python3} setup.py build)
(cd desktop; %{__python3} setup.py build)
%install
(cd cli; %{__python3} setup.py install --skip-build --root %{buildroot})
(cd desktop; %{__python3} setup.py install --skip-build --root %{buildroot})
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
