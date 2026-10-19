%global source0_hash 285f0be722bcef00f865e2f4f535c8a612fc7f26eba0ab2d0052b4aac12aa470
Name:           python-zoidberg
Version:        0.3.1
Release:        1%{?dist}
Summary:        Generate flux-coordinate independent _FCI_ grids for BOUT++
License:        LGPL-3.0-or-later
URL:            https://github.com/boutproject/zoidberg
Source0:        https://files.pythonhosted.org/packages/source/z/zoidberg/zoidberg-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-zoidberg = %{version}-%{release}
# /oreon:deps
%package -n       python3-zoidberg+tests
Summary:        Metapackage for python3-zoidberg tests extras
Requires:       python3-zoidberg = %{version}-%{release}
Requires:       python3dist(pytest) >= 3.3.0
Provides:       python3dist(zoidberg[tests]) = %{version}-%{release}

%description -n python3-zoidberg+tests
Metapackage for python3-zoidberg tests extras.

%description

%package -n     python3-zoidberg
Summary:        Generate flux-coordinate independent _FCI_ grids for BOUT++
# oreon:reqs
Requires:       python3dist(boutdata) >= 0.3
Requires:       python3dist(freeqdsk) >= 0.4.0
Requires:       python3dist(matplotlib) >= 3.8.0
Requires:       python3dist(netcdf4) >= 1.7
Requires:       python3dist(numpy) >= 2.0.0
Requires:       python3dist(scipy) >= 1.12.0
Requires:       python3dist(sympy) >= 1.7
# /oreon:reqs
%description -n python3-zoidberg

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zoidberg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zoidberg usr/lib/python3*/site-packages/zoidberg* usr/lib64/python3*/site-packages/zoidberg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zoidberg* usr/lib64/python3*/site-packages/zoidberg* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zoidberg -f %{oreon_filedir}/python3-zoidberg.list

%changelog

%autochangelog
