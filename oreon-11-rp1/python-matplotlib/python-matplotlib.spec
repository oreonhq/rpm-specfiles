%global source0_hash cec596316640f2b394b8f0daa0ea61a8eae82d017b620b9f202befb972a59ea4
Name:           python-matplotlib
Version:        3.11.2
Release:        1%{?dist}
Summary:        Python plotting package
License:        PSF-2.0
URL:            https://matplotlib.org
Source0:        https://files.pythonhosted.org/packages/source/m/matplotlib/matplotlib-%{version}.tar.gz
Patch1001:      0001-matplotlibrc-path-search-fix.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(meson-python) >= 0.13.2
BuildRequires:  python3dist(pybind11) >= 2.13.2
BuildRequires:  python3dist(setuptools-scm) < 10
BuildRequires:  python3dist(setuptools-scm) >= 7
Requires:       python3-matplotlib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-matplotlib
Summary:        Python plotting package
# oreon:reqs
Requires:       python3dist(contourpy) >= 1.0.1
Requires:       python3dist(cycler) >= 0.10
Requires:       python3dist(fonttools) >= 4.28.2
Requires:       python3dist(kiwisolver) >= 1.3.1
Requires:       python3dist(numpy) >= 1.25
Requires:       python3dist(packaging) >= 20.0
Requires:       python3dist(pillow) >= 9
Requires:       python3dist(pyparsing) >= 3
Requires:       python3dist(python-dateutil) >= 2.7
# /oreon:reqs
%description -n python3-matplotlib

%prep
%global oreon_srcdir matplotlib-%{version}
%oreon_prep
%build

%pyproject_wheel -Csetup-args=-Dsystem-freetype=true -Csetup-args=-Dsystem-libraqm=true -Csetup-args=-Dsystem-qhull=true
%install
%pyproject_install
%oreon_autofiles python3-matplotlib usr/lib/python3*/site-packages/matplotlib* usr/lib64/python3*/site-packages/matplotlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/matplotlib* usr/lib64/python3*/site-packages/matplotlib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-matplotlib -f %{oreon_filedir}/python3-matplotlib.list

%changelog

%autochangelog
