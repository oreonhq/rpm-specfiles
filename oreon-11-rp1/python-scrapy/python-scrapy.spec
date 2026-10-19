%global source0_hash 34130726582b64c91531162ab277c4053e558876d49ba219cb43679e71d80a87
Name:           python-scrapy
Version:        2.19.0
Release:        1%{?dist}
Summary:        A high-level Web Crawling and Web Scraping framework
License:        BSD-3-Clause
URL:            https://scrapy.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scrapy/scrapy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-scrapy = %{version}-%{release}
# /oreon:deps
%package -n       python3-scrapy+bpython
Summary:        Metapackage for python3-scrapy bpython extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(bpython) >= 0.7.1
Provides:       python3dist(scrapy[bpython]) = %{version}-%{release}

%description -n python3-scrapy+bpython
Metapackage for python3-scrapy bpython extras.

%package -n       python3-scrapy+color
Summary:        Metapackage for python3-scrapy color extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(colorlog) >= 6.6.0
Provides:       python3dist(scrapy[color]) = %{version}-%{release}

%description -n python3-scrapy+color
Metapackage for python3-scrapy color extras.

%package -n       python3-scrapy+gcs
Summary:        Metapackage for python3-scrapy gcs extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(google-cloud-storage) >= 1.29.0
Provides:       python3dist(scrapy[gcs]) = %{version}-%{release}

%description -n python3-scrapy+gcs
Metapackage for python3-scrapy gcs extras.

%package -n       python3-scrapy+httpx
Summary:        Metapackage for python3-scrapy httpx extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(httpx2[http2,socks]) >= 2.0.0
Provides:       python3dist(scrapy[httpx]) = %{version}-%{release}

%description -n python3-scrapy+httpx
Metapackage for python3-scrapy httpx extras.

%package -n       python3-scrapy+images
Summary:        Metapackage for python3-scrapy images extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(pillow) >= 8.3.2
Provides:       python3dist(scrapy[images]) = %{version}-%{release}

%description -n python3-scrapy+images
Metapackage for python3-scrapy images extras.

%package -n       python3-scrapy+ipython
Summary:        Metapackage for python3-scrapy ipython extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(ipython) >= 8.15.0
Provides:       python3dist(scrapy[ipython]) = %{version}-%{release}

%description -n python3-scrapy+ipython
Metapackage for python3-scrapy ipython extras.

%package -n       python3-scrapy+ptpython
Summary:        Metapackage for python3-scrapy ptpython extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(ptpython) >= 3.0.23
Provides:       python3dist(scrapy[ptpython]) = %{version}-%{release}

%description -n python3-scrapy+ptpython
Metapackage for python3-scrapy ptpython extras.

%package -n       python3-scrapy+robotparser
Summary:        Metapackage for python3-scrapy robotparser extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(robotexclusionrulesparser) >= 1.6.2
Provides:       python3dist(scrapy[robotparser]) = %{version}-%{release}

%description -n python3-scrapy+robotparser
Metapackage for python3-scrapy robotparser extras.

%package -n       python3-scrapy+s3
Summary:        Metapackage for python3-scrapy s3 extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.20.0
Provides:       python3dist(scrapy[s3]) = %{version}-%{release}

%description -n python3-scrapy+s3
Metapackage for python3-scrapy s3 extras.

%package -n       python3-scrapy+twisted-http2
Summary:        Metapackage for python3-scrapy twisted-http2 extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(twisted[http2]) >= 21.7.0
Provides:       python3dist(scrapy[twisted-http2]) = %{version}-%{release}

%description -n python3-scrapy+twisted-http2
Metapackage for python3-scrapy twisted-http2 extras.

%package -n       python3-scrapy+uvloop
Summary:        Metapackage for python3-scrapy uvloop extras
Requires:       python3-scrapy = %{version}-%{release}
Requires:       python3dist(uvloop) >= 0.16.0
Provides:       python3dist(scrapy[uvloop]) = %{version}-%{release}

%description -n python3-scrapy+uvloop
Metapackage for python3-scrapy uvloop extras.

%description

%package -n     python3-scrapy
Summary:        A high-level Web Crawling and Web Scraping framework
# oreon:reqs
Requires:       python3dist(aiohttp) >= 3.13.3
Requires:       python3dist(backports.zstd) >= 1.3.0
Requires:       python3dist(brotli) >= 1.2.0
Requires:       python3dist(brotlicffi) >= 1.2.0.0
Requires:       python3dist(charset-normalizer) >= 3.4.0
Requires:       python3dist(cryptography) >= 41.0.5
Requires:       python3dist(cssselect) >= 0.9.1
Requires:       python3dist(defusedxml) >= 0.7.1
Requires:       python3dist(itemadapter) >= 0.1.0
Requires:       python3dist(itemloaders) >= 1.0.1
Requires:       python3dist(lxml) >= 4.6.4
Requires:       python3dist(parsel) >= 1.5.0
Requires:       python3dist(platformdirs) >= 2.0.0
Requires:       python3dist(protego) >= 0.1.15
Requires:       python3dist(pydispatcher) >= 2.0.5
Requires:       python3dist(pyopenssl) >= 24.3.0
Requires:       python3dist(pypydispatcher) >= 2.1.0
Requires:       python3dist(queuelib) >= 1.6.1
Requires:       python3dist(service-identity) >= 24.2.0
Requires:       python3dist(twisted) >= 21.7.0
Requires:       python3dist(w3lib) >= 2.1.1
Requires:       python3dist(zope.interface) >= 5.1.0
# /oreon:reqs
%description -n python3-scrapy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir scrapy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scrapy usr/lib/python3*/site-packages/scrapy* usr/lib64/python3*/site-packages/scrapy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scrapy* usr/lib64/python3*/site-packages/scrapy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-scrapy -f %{oreon_filedir}/python3-scrapy.list

%changelog

%autochangelog
