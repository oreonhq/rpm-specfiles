%global source0_hash 2964ca058cf93f2917048ee3ff03907cf65f8f2034de09992b52063801a91790
Name:           python-commoncode
Version:        32.5.2
Release:        1%{?dist}
Summary:        Set of common utilities, originally split from ScanCode
License:        ...
URL:            https://github.com/nexB/scancode-toolkit
Source0:        https://files.pythonhosted.org/packages/source/c/commoncode/commoncode-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flot) >= 0.7.0
Requires:       python3-commoncode = %{version}-%{release}
# /oreon:deps
%package -n       python3-commoncode+dev
Summary:        Metapackage for python3-commoncode dev extras
Requires:       python3-commoncode = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0.1
Requires:       python3dist(pytest-xdist) >= 2
Requires:       python3dist(aboutcode-toolkit) >= 11.1.1
Requires:       python3dist(pycodestyle) >= 2.8.0
Requires:       python3dist(sphinx) >= 5.0.2
Requires:       python3dist(sphinx-rtd-theme) >= 1.0.0
Requires:       python3dist(sphinx-reredirects) >= 0.1.2
Requires:       python3dist(doc8) >= 0.11.2
Requires:       python3dist(sphinx-rtd-dark-mode) >= 1.3.0
Provides:       python3dist(commoncode[dev]) = %{version}-%{release}

%description -n python3-commoncode+dev
Metapackage for python3-commoncode dev extras.

%description

%package -n     python3-commoncode
Summary:        Set of common utilities, originally split from ScanCode
# oreon:reqs
Requires:       python3dist(attrs) >= 18.1
Requires:       python3dist(attrs) >= 22.1.0
Requires:       python3dist(beautifulsoup4[chardet]) >= 4.13.0
Requires:       python3dist(click) >= 8.3.0
Requires:       python3dist(requests[use_chardet_on_py3]) >= 2.7.0
Requires:       python3dist(saneyaml) >= 0.5.2
Requires:       python3dist(text-unidecode) >= 1.0
# /oreon:reqs
%description -n python3-commoncode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir commoncode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-commoncode usr/lib/python3*/site-packages/commoncode* usr/lib64/python3*/site-packages/commoncode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/commoncode* usr/lib64/python3*/site-packages/commoncode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-commoncode -f %{oreon_filedir}/python3-commoncode.list

%changelog

%autochangelog
