%global source0_hash c9bf500e9423a96e8018510ed9899631cd37d5b4ffcb5de90279acc73c835cc6
Name:           python-boutdata
Version:        0.4.0
Release:        1%{?dist}
Summary:        Python package for collecting BOUT++ data
License:        LGPL-3.0-or-later
URL:            https://github.com/boutproject/boutdata
Source0:        https://files.pythonhosted.org/packages/source/b/boutdata/boutdata-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/boutproject/boutdata/pull/126.patch
Patch:          https://github.com/boutproject/boutdata/pull/125.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-boutdata = %{version}-%{release}
# /oreon:deps
%package -n       python3-boutdata+tests
Summary:        Metapackage for python3-boutdata tests extras
Requires:       python3-boutdata = %{version}-%{release}
Provides:       python3dist(boutdata[tests]) = %{version}-%{release}

%description -n python3-boutdata+tests
Metapackage for python3-boutdata tests extras.

%package -n       python3-boutdata+docs
Summary:        Metapackage for python3-boutdata docs extras
Requires:       python3-boutdata = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.4
Requires:       python3dist(sphinx) < 5
Provides:       python3dist(boutdata[docs]) = %{version}-%{release}

%description -n python3-boutdata+docs
Metapackage for python3-boutdata docs extras.

%package -n       python3-boutdata+lint
Summary:        Metapackage for python3-boutdata lint extras
Requires:       python3-boutdata = %{version}-%{release}
Provides:       python3dist(boutdata[lint]) = %{version}-%{release}

%description -n python3-boutdata+lint
Metapackage for python3-boutdata lint extras.

%description

%package -n     python3-boutdata
Summary:        Python package for collecting BOUT++ data
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.8.0
Requires:       python3dist(natsort) >= 8.1.0
Requires:       python3dist(numpy) >= 1.26.0
Requires:       python3dist(scipy) >= 1.12.0
Requires:       python3dist(sympy) >= 1.5.1
# /oreon:reqs
%description -n python3-boutdata

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir boutdata-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-boutdata usr/lib/python3*/site-packages/boutdata* usr/lib64/python3*/site-packages/boutdata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/boutdata* usr/lib64/python3*/site-packages/boutdata* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-boutdata -f %{oreon_filedir}/python3-boutdata.list

%changelog

%autochangelog
