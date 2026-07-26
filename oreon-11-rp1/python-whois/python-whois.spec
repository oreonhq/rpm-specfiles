%global source0_hash 6708f15329ebd986a8ed7c55faf59a879c5f7d8a88bb10a4c8872a1006e4a623

%global pypi_name whois

%global pypi_description Python wrapper for the "whois" command with \
a simple interface to access parsed WHOIS data for a given domain, \
able to extract data for all the popular TLDs (com, org, net, biz, info...).

Name: python-%{pypi_name}
Summary: Python module for retrieving WHOIS information of domains
License: MIT

Version: 0.9.27
Release: 13%{?dist}

URL: https://github.com/DannyCork/python-whois/
Source0: %{URL}archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: whois

%description
%pypi_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%pypi_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%py3_build

%install
%py3_install

%check
./test.sh

%files -n python3-%{pypi_name}
%license license
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info

%changelog
%autochangelog
