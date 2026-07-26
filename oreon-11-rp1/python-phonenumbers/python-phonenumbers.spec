%global source0_hash a5380121d4411f0b614470fa900fd49436a998e80a56f590f63bfc79fede18b3

%global pypi_name phonenumbers

%global desc A Python port of libphonenumber, Google's common Java, C++, and\
JavaScript library for parsing, formatting, and validating international phone\
numbers.\

Name:           python-%{pypi_name}
Version:        8.13.48
Release:        7%{?dist}
Summary:        A Python port of Google's libphonenumber
License:        Apache-2.0
URL:            https://github.com/daviddrysdale/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Snip the #! from the util.py module
sed -i -e '/^#!\//, 1d' python/%{pypi_name}/util.py

%build
cd python
%py3_build

%install
cd python
%py3_install

%check
cd python
%{__python3} ./testwrapper.py -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%changelog
%autochangelog
