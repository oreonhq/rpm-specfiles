%global source0_hash c9d91274e5f55835e12b524adf1f231739ea811a8866d810e5bb42ba87cd8eda
Name:           python-selenium
Version:        4.49.0
Release:        1%{?dist}
Summary:        Official Python bindings for Selenium WebDriver
License:        Apache-2.0
URL:            https://www.selenium.dev
Source0:        https://files.pythonhosted.org/packages/source/s/selenium/selenium-%{version}.tar.gz
BuildArch:      noarch
Patch1:        selenium-use-without-bundled-libs.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-selenium = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-selenium
Summary:        Official Python bindings for Selenium WebDriver
# oreon:reqs
Requires:       python3dist(certifi) >= 2026.2.25
Requires:       python3dist(trio) < 1.0
Requires:       python3dist(trio) >= 0.31.0
Requires:       python3dist(trio-websocket) < 1.0
Requires:       python3dist(trio-websocket) >= 0.12.2
Requires:       python3dist(typing-extensions) < 5.0
Requires:       python3dist(typing-extensions) >= 4.15.0
Requires:       python3dist(urllib3[socks]) < 3.0
Requires:       python3dist(urllib3[socks]) >= 2.6.3
Requires:       python3dist(websocket-client) < 2.0
Requires:       python3dist(websocket-client) >= 1.8.0
# /oreon:reqs
%description -n python3-selenium

%prep
%global oreon_srcdir selenium-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-selenium usr/lib/python3*/site-packages/selenium* usr/lib64/python3*/site-packages/selenium* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/selenium* usr/lib64/python3*/site-packages/selenium* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-selenium -f %{oreon_filedir}/python3-selenium.list

%changelog

%autochangelog
