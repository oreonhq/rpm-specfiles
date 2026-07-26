%global source0_hash 4faf5b3abe83bf014476e3fd9ccf66867282971d9f1d4e96d9a61b60c3786770

%global srcname itemloaders
%global desc %{expand:
itemloaders is a library that helps you collect data from HTML and XML sources.

It comes in handy to extract data from web pages, as it supports data extraction
using CSS and XPath Selectors.

It's specially useful when you need to standardize the data from many sources.
For example, it allows you to have all your casting and parsing rules in a 
single place.}

Name:		python-itemloaders
Version:	1.3.2
Release:	7%{?dist}
Summary:	Library that helps you collect data from HTML and XML sources.

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/scrapy/itemloaders
Source0:	%{pypi_source}

BuildArch:	noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-parsel
BuildRequires:	python3-jmespath
BuildRequires:	python3-w3lib

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/itemloaders
%{python3_sitelib}/itemloaders-*.egg-info

%changelog
%autochangelog
