%global source0_hash 7820a7e6cfaee455f4ca75eb806568772f471b62fbd613fe6a7fac52d3970a92
Name:           python-pyvlx
Version:        0.2.36
Release:        1%{?dist}
Summary:        PyVLX is a wrapper for the Velux KLF 200 API. PyVLX enables you to run scenes and or open and close velux windows.
License:        LGPL-3.0-or-later
URL:            https://github.com/Julius2342/pyvlx
Source0:        https://files.pythonhosted.org/packages/source/p/pyvlx/pyvlx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm) >= 8.0
Requires:       python3-pyvlx = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyvlx+dev
Summary:        Metapackage for python3-pyvlx dev extras
Requires:       python3-pyvlx = %{version}-%{release}
Requires:       python3dist(pytest) == 9.1.0
Requires:       python3dist(pytest-cov) == 7.1.0
Requires:       python3dist(mypy) == 2.1.0
Requires:       python3dist(types-pyyaml) == 6.0.12.20260518
Requires:       python3dist(isort) == 8.0.1
Requires:       python3dist(flake8) == 7.3.0
Requires:       python3dist(flake8-isort) == 7.0.0
Requires:       python3dist(flake8-pyproject) == 1.2.4
Requires:       python3dist(pydocstyle) == 6.3.0
Requires:       python3dist(pylint) == 4.0.6
Provides:       python3dist(pyvlx[dev]) = %{version}-%{release}

%description -n python3-pyvlx+dev
Metapackage for python3-pyvlx dev extras.

%package -n       python3-pyvlx+release
Summary:        Metapackage for python3-pyvlx release extras
Requires:       python3-pyvlx = %{version}-%{release}
Requires:       python3dist(build) == 1.5.0
Requires:       python3dist(twine) == 6.2.0
Provides:       python3dist(pyvlx[release]) = %{version}-%{release}

%description -n python3-pyvlx+release
Metapackage for python3-pyvlx release extras.

%description

%package -n     python3-pyvlx
Summary:        PyVLX is a wrapper for the Velux KLF 200 API. PyVLX enables you to run scenes and or open and close velux windows.
# oreon:reqs
Requires:       python3dist(pyyaml) < 7.0
Requires:       python3dist(pyyaml) >= 6.0
Requires:       python3dist(zeroconf) >= 0.148
# /oreon:reqs
%description -n python3-pyvlx

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyvlx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyvlx usr/lib/python3*/site-packages/pyvlx* usr/lib64/python3*/site-packages/pyvlx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyvlx* usr/lib64/python3*/site-packages/pyvlx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyvlx -f %{oreon_filedir}/python3-pyvlx.list

%changelog

%autochangelog
