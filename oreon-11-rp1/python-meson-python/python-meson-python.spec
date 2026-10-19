%global source0_hash 9c819d0d4efa746edadfaae4663c0e9c75659186ef7e5bab12330bfe22964dfc
Name:           python-meson-python
Version:        0.22.0
Release:        1%{?dist}
Summary:        The Python build backend for Meson projects
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source0:        https://files.pythonhosted.org/packages/source/m/meson_python/meson_python-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(meson) >= 0.64.0
BuildRequires:  python3dist(meson) >= 1.2.3
BuildRequires:  python3dist(packaging) >= 23.2
BuildRequires:  python3dist(packaging) >= 24.2
BuildRequires:  python3dist(pyproject-metadata) >= 0.9.0
BuildRequires:  python3dist(tomli) >= 1.0.0
Requires:       python3-meson-python = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-meson-python
Summary:        The Python build backend for Meson projects
# oreon:reqs
Requires:       python3dist(meson) >= 0.64.0
Requires:       python3dist(meson) >= 1.2.3
Requires:       python3dist(packaging) >= 23.2
Requires:       python3dist(packaging) >= 24.2
Requires:       python3dist(pyproject-metadata) >= 0.9.0
Requires:       python3dist(tomli) >= 1.0.0
# /oreon:reqs
%description -n python3-meson-python

%prep
%global oreon_srcdir meson_python-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-meson-python usr/lib/python3*/site-packages/meson_python* usr/lib64/python3*/site-packages/meson_python* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/meson_python* usr/lib64/python3*/site-packages/meson_python* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-meson-python -f %{oreon_filedir}/python3-meson-python.list

%changelog

%autochangelog
