%global source0_hash 186a0b41a94524f0984d085ca6b945c79a254465b7097f2560dc0c04e8d1d8a5

%global srcname pymediainfo

Name:           python-%{srcname}
Version:        6.1.0
Release:        12%{?dist}
Summary:        Python wrapper around the MediaInfo library

License:        MIT
URL:            https://github.com/sbraz/%{srcname}
Source0:        https://pypi.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  libmediainfo

%description
%{sum}.

%package     -n python3-%{srcname}
Summary:        Python3 wrapper around the MediaInfo library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools_scm
Requires:       libmediainfo
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This small package is a Python3 wrapper around the MediaInfo library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
export LC_ALL=C.UTF-8
%pytest -k "not test_parse_url"

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/%{srcname}*

%changelog
%autochangelog
