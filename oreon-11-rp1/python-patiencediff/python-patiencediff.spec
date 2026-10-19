%global source0_hash a060953edd05521e6368245d6c70402308a7aea4f66a706b2d832721d1375679
Name:           python-patiencediff
Version:        0.2.19
Release:        1%{?dist}
Summary:        Python implementation of the patiencediff algorithm
License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org/
Source0:        https://files.pythonhosted.org/packages/source/p/patiencediff/patiencediff-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
BuildRequires:  python3dist(setuptools-rust) >= 1.5.0
Requires:       python3-patiencediff = %{version}-%{release}
# /oreon:deps
%package -n       python3-patiencediff+dev
Summary:        Metapackage for python3-patiencediff dev extras
Requires:       python3-patiencediff = %{version}-%{release}
Requires:       python3dist(ruff) == 0.14.10
Requires:       python3dist(mypy) >= 1.0.0
Provides:       python3dist(patiencediff[dev]) = %{version}-%{release}

%description -n python3-patiencediff+dev
Metapackage for python3-patiencediff dev extras.

%description

%package -n     python3-patiencediff
Summary:        Python implementation of the patiencediff algorithm
%description -n python3-patiencediff

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir patiencediff-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-patiencediff usr/lib/python3*/site-packages/patiencediff* usr/lib64/python3*/site-packages/patiencediff* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/patiencediff* usr/lib64/python3*/site-packages/patiencediff* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-patiencediff -f %{oreon_filedir}/python3-patiencediff.list

%changelog

%autochangelog
