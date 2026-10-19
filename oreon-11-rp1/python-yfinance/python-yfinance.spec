%global source0_hash 442f780d13d3e52fefa6c721c2c9bfee321078c1987d6585ec193b5c24382f8a
Name:           python-yfinance
Version:        1.7.0
Release:        1%{?dist}
Summary:        Download market data from Yahoo! Finance API
License:        Apache-2.0
URL:            https://github.com/ranaroussi/yfinance
Source0:        https://files.pythonhosted.org/packages/source/y/yfinance/yfinance-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-yfinance = %{version}-%{release}
# /oreon:deps
%package -n       python3-yfinance+repair
Summary:        Metapackage for python3-yfinance repair extras
Requires:       python3-yfinance = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.6.3
Requires:       python3dist(scikit-learn) >= 1.0
Provides:       python3dist(yfinance[repair]) = %{version}-%{release}

%description -n python3-yfinance+repair
Metapackage for python3-yfinance repair extras.

%package -n       python3-yfinance+dev
Summary:        Metapackage for python3-yfinance dev extras
Requires:       python3-yfinance = %{version}-%{release}
Requires:       python3dist(jinja2) == 3.1.4
Requires:       python3dist(pydata-sphinx-theme) == 0.15.4
Requires:       python3dist(pytest) >= 9.0.3
Requires:       python3dist(pytest-cov) >= 7.1.0
Requires:       python3dist(ruff) >= 0.15.16
Requires:       python3dist(sphinx) == 8.0.2
Requires:       python3dist(sphinx-copybutton) == 0.5.2
Provides:       python3dist(yfinance[dev]) = %{version}-%{release}

%description -n python3-yfinance+dev
Metapackage for python3-yfinance dev extras.

%description

%package -n     python3-yfinance
Summary:        Download market data from Yahoo! Finance API
# oreon:reqs
Requires:       python3dist(beautifulsoup4) >= 4.11.1
Requires:       python3dist(curl-cffi) >= 0.15
Requires:       python3dist(lxml) >= 4.9.0
Requires:       python3dist(multitasking) >= 0.0.7
Requires:       python3dist(numpy) >= 1.16.5
Requires:       python3dist(pandas) >= 1.3.0
Requires:       python3dist(peewee) >= 3.16.2
Requires:       python3dist(platformdirs) >= 2.0.0
Requires:       python3dist(protobuf) >= 3.19.0
Requires:       python3dist(pytz) >= 2022.5
Requires:       python3dist(requests) >= 2.31
Requires:       python3dist(websockets) >= 13.0
# /oreon:reqs
%description -n python3-yfinance

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir yfinance-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-yfinance usr/lib/python3*/site-packages/yfinance* usr/lib64/python3*/site-packages/yfinance* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/yfinance* usr/lib64/python3*/site-packages/yfinance* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-yfinance -f %{oreon_filedir}/python3-yfinance.list

%changelog

%autochangelog
