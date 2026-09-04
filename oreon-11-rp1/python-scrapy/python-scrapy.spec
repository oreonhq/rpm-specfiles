%global source0_hash 2445f8b5bf87ba105d239cb230878646e29dbc6a6cae10037ba0550d8fe7fc73

%global pypi_name Scrapy
%global pkg_name scrapy
Name:		python-scrapy
Version:	2.18.0
Release:	1%{?dist}
Summary:	A high-level Python Screen Scraping framework
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://scrapy.org
# TODO fix Source0 to correct github source URL
Source0:	https://files.pythonhosted.org/packages/source/S/%{pypi_name}/%{pkg_name}-%{version}.tar.gz
BuildArch:	noarch

%description
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.

%package -n python3-%{pkg_name}
Summary:	%{summary}

Requires:	python3-pyOpenSSL
Requires:	python3-twisted
Requires:	python3-lxml
Requires:	python3-w3lib
Requires:	python3-queuelib
Requires:	python3-zope-interface
Requires:	python3-cssselect
Requires:	python3-pydispatcher
Requires:	python3-parsel
Requires:	python3-itemadapter
Requires:	python3-protego
Requires:	python3-itemloaders
Requires:	python3-pydispatcher
Requires:	python-tldextract
Requires:	python3-service-identity
Requires:	python3-cryptography 

%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.

%package doc
Summary:	Documentation for %{name}

%description doc
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.
This package contains the documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel
pushd docs
%make_build html && rm -r build/html/.buildinfo
popd

%install
%pyproject_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc AUTHORS PKG-INFO
%{python3_sitelib}/scrapy
%{python3_sitelib}/scrapy-%{version}.dist-info/
%{_bindir}/scrapy

%changelog
%autochangelog
