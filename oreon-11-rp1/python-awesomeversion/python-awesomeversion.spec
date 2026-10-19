%global source0_hash e6cd08c90292a11f30b8de401863dcde7bc66a671d8173f9066ebd15d9310453
Name:           python-awesomeversion
Version:        25.8.0
Release:        1%{?dist}
Summary:        One version package to rule them all, One version package to find them, One version package to bring them all, and in the darkness bind them.
License:        MIT
URL:            https://github.com/ludeeus/awesomeversion
Source0:        https://files.pythonhosted.org/packages/source/a/awesomeversion/awesomeversion-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-awesomeversion = %{version}-%{release}
# /oreon:deps
%package -n       python3-awesomeversion+dev
Summary:        Metapackage for python3-awesomeversion dev extras
Requires:       python3-awesomeversion = %{version}-%{release}
Requires:       python3dist(black) >= 25.1
Requires:       python3dist(isort) >= 6.0.1
Requires:       python3dist(mypy) >= 1.16
Requires:       python3dist(pylint) >= 3.3.7
Requires:       python3dist(pytest) >= 8.4.1
Requires:       python3dist(pytest-codspeed) >= 3.2.0
Requires:       python3dist(pytest-cov) >= 6.2.1
Requires:       python3dist(pytest-snapshot) >= 0.9.0
Requires:       python3dist(pytest-timeout) >= 2.4.0
Provides:       python3dist(awesomeversion[dev]) = %{version}-%{release}

%description -n python3-awesomeversion+dev
Metapackage for python3-awesomeversion dev extras.

%description

%package -n     python3-awesomeversion
Summary:        One version package to rule them all, One version package to find them, One version package to bring them all, and in the darkness bind them.
%description -n python3-awesomeversion

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir awesomeversion-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-awesomeversion usr/lib/python3*/site-packages/awesomeversion* usr/lib64/python3*/site-packages/awesomeversion* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/awesomeversion* usr/lib64/python3*/site-packages/awesomeversion* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-awesomeversion -f %{oreon_filedir}/python3-awesomeversion.list

%changelog

%autochangelog
