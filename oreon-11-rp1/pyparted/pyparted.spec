%global source0_hash 8fc6758abd16c7b0429fd4c07b6a7672678d493bfe1811040cd77d45e04964ea
%global source1_hash 5d23cced3ced5ed45276b48cf53f4250d28028cc23279c9c347ffb48fb0e5c9d

Summary:       Python module for GNU parted
Name:          pyparted
Epoch:         1
Version:       3.13.0
Release:       %autorelease
License:       GPL-2.0-or-later
URL:           https://github.com/dcantrell/pyparted

Source0:       https://github.com/dcantrell/pyparted/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:       https://github.com/dcantrell/pyparted/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:       keyring.gpg
Source3:       trustdb.gpg

BuildRequires: make
BuildRequires: gcc
BuildRequires: parted-devel >= 3.4
BuildRequires: pkgconfig
BuildRequires: e2fsprogs
BuildRequires: gnupg2
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%package -n python3-pyparted
Summary: Python 3 module for GNU parted

%description -n python3-pyparted
Python module for the parted library.  It is used for manipulating
partition tables. This package provides Python 3 bindings for parted.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
# Verify source archive signature
gpg --no-default-keyring --keyring %{SOURCE2} --trustdb-name %{SOURCE3} --verify %{SOURCE1} %{SOURCE0} || exit 1

%autosetup

%build
%make_build CFLAGS="%{optflags} -fcommon"

%check
make test

%install
%make_install

%files -n python3-pyparted
%doc AUTHORS HACKING NEWS README.md RELEASE TODO
%license LICENSE
%{python3_sitearch}/_ped.*.so
%{python3_sitearch}/parted
%{python3_sitearch}/%{name}-%{version}-*.egg-info

%changelog
%autochangelog
