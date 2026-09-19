%global source0_hash d6342277da1a51d347fe55fa22140e60170dcd5476d8550c7a4e2c4838ec95e0

%global snapdate 20110209
%global module openoffice

Name:           python-%{module}
Version:        0.1
Release:        0.55.%{snapdate}%{?dist}
Summary:        Python libraries for interacting with LibreOffice
License:        GPL-3.0-only AND LGPL-2.1-or-later
URL:            https://gitorious.org/openoffice-python
Source0:        https://pypi.python.org/packages/source/o/openoffice-python/%{module}-python-%{version}-%{snapdate}.tar.bz2
Patch0:         python-openoffice-2to3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
The library is designed to supports both writing Macros (called by OOo) and\
interacting with OOo from an external Python program (using the UNO bridge).

%description %_description

%package -n python3-%{module}
Summary:        Python 3 libraries for interacting with LibreOffice

%description -n python3-%{module}
The library is designed to supports both writing Macros (called by OOo) and
interacting with OOo from an external Python program (using the UNO bridge).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{module}-python-%{version}-%{snapdate}
%patch -P 0 -p1

# remove exec perms for docs
chmod a-x sample-scripts/*

# remove the shebang line
sed -i -e '1d' %{module}/streams.py
sed -i -e '1d' %{module}/interact.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%license COPYING LICENSE-gpl-3.0.txt
%doc README sample-scripts
%{python3_sitelib}/*

%changelog
%autochangelog
