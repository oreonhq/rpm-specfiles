%global source0_hash a1de4b43f6e1edbb39a6fcc1e1339856c7c7584d2899312d69449ad22f2834e7

%global _hardened_build 1

Name:           onionshare
Version:        2.5
Release:        16%{?dist}
Summary:        Securely and anonymously share files of any size

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://onionshare.org/
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz

#Patch0:        % {name}-appdata.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       python3-flask
Requires:       python3-stem
Requires:       python3-qt5
Requires:       nautilus-python
Requires:       tor

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

#desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
#mkdir -p %{buildroot}%{_datadir}/appdata/
#install -m 644 %{_builddir}/%{name}-%{version}/install/%{name}.appdata.xml \
#    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
#chmod +x %{buildroot}/%{_datadir}/nautilus-python/extensions/%{name}-nautilus*

%check
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc LICENSE README.md
%{_bindir}/*
%{python3_sitelib}/%{name}*

#% {_datadir}/doc/onionshare/*
#% aappdata/% {name}.*
#% {_datadir}/pixmaps/*
#% {_datadir}/% {name}/*
#% {_datadir}/applications/*
#% {_datadir}/nautilus-python/extensions/% {name}-nautilus*
#% {_bindir}/% {name}-gui

%changelog
%autochangelog
