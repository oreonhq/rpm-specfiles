%global source0_hash 480543731c5fcdd17b60613ed8b5ad256bb5b7bb761c40493a6af6cd148b5ea7

%global         hguser         techtonik
%global         srcname        hexdump
# 2016-08-18
%global         commit         66325cb5fed890df4a345e25ea8f107fd31b60d8
%global         commitdate     20160818
%global         shortcommit    %(c=%{commit}; echo ${c:0:12})

Name:           python-hexdump
Version:        3.4
Release:        0.32.%{commitdate}hg%{shortcommit}%{?dist}
Summary:        Dump binary data to hex format and restore from there

License:        LicenseRef-Fedora-Public-Domain
#               https://pypi.python.org/pypi/hexdump
#               https://bitbucket.org/techtonik/hexdump
URL:            https://bitbucket.com/%{hguser}/%{srcname}
Source0:        https://bitbucket.org/%{hguser}/%{srcname}/get/%{shortcommit}.zip#/%{name}-%{version}-%{shortcommit}.zip
Source1:        hexdumpy.1

# Create the /usr/bin/hexdumpy
# https://bitbucket.org/techtonik/hexdump/pull-requests/5/modify-the-setuppy-in-order-to-generate/diff
Patch0:         %{name}-setup.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Python library to dump binary data to hex format and restore from there

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Dump binary data to hex format and restore from there
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Python library to dump binary data to hex format and restore from there

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{hguser}-%{srcname}-%{shortcommit}
%patch -P0 -p 1 -b .setup
sed -i -e 's|#!/usr/bin/env python|#|' hexdump.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hexdumpy.1

%files -n python%{python3_pkgversion}-%{srcname}
%license UNLICENSE
%doc README.txt
%{python3_sitelib}/*
%{_bindir}/hexdumpy
%{_mandir}/man1/hexdumpy.1*

%changelog
%autochangelog
