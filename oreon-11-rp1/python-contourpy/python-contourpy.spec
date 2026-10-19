%global source0_hash 20156f5a1ac4f8ce02656e39a61e82164a3d359796dc8026f75b062783d500e1
Name:           python-contourpy
Version:        1.4.0
Release:        1%{?dist}
Summary:        Python library for calculating contours of 2D quadrilateral grids
License:        BSD-3-Clause
URL:            https://github.com/contourpy/contourpy
Source0:        https://files.pythonhosted.org/packages/source/c/contourpy/contourpy-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(meson-python) >= 0.18.0
BuildRequires:  python3dist(pybind11) >= 2.13.2
Requires:       python3-contourpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-contourpy+docs
Summary:        Metapackage for python3-contourpy docs extras
Requires:       python3-contourpy = %{version}-%{release}
Provides:       python3dist(contourpy[docs]) = %{version}-%{release}

%description -n python3-contourpy+docs
Metapackage for python3-contourpy docs extras.

%package -n       python3-contourpy+bokeh
Summary:        Metapackage for python3-contourpy bokeh extras
Requires:       python3-contourpy = %{version}-%{release}
Provides:       python3dist(contourpy[bokeh]) = %{version}-%{release}

%description -n python3-contourpy+bokeh
Metapackage for python3-contourpy bokeh extras.

%package -n       python3-contourpy+mypy
Summary:        Metapackage for python3-contourpy mypy extras
Requires:       python3-contourpy = %{version}-%{release}
Requires:       python3dist(mypy) == 2.1.0
Provides:       python3dist(contourpy[mypy]) = %{version}-%{release}

%description -n python3-contourpy+mypy
Metapackage for python3-contourpy mypy extras.

%package -n       python3-contourpy+test
Summary:        Metapackage for python3-contourpy test extras
Requires:       python3-contourpy = %{version}-%{release}
Provides:       python3dist(contourpy[test]) = %{version}-%{release}

%description -n python3-contourpy+test
Metapackage for python3-contourpy test extras.

%package -n       python3-contourpy+test-no-images
Summary:        Metapackage for python3-contourpy test-no-images extras
Requires:       python3-contourpy = %{version}-%{release}
Requires:       python3dist(pytest-rerunfailures) < 16
Provides:       python3dist(contourpy[test-no-images]) = %{version}-%{release}

%description -n python3-contourpy+test-no-images
Metapackage for python3-contourpy test-no-images extras.

%description

%package -n     python3-contourpy
Summary:        Python library for calculating contours of 2D quadrilateral grids
# oreon:reqs
Requires:       python3dist(numpy) >= 2.0
# /oreon:reqs
%description -n python3-contourpy

%prep
%global oreon_srcdir contourpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-contourpy usr/lib/python3*/site-packages/contourpy* usr/lib64/python3*/site-packages/contourpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/contourpy* usr/lib64/python3*/site-packages/contourpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-contourpy -f %{oreon_filedir}/python3-contourpy.list

%changelog

%autochangelog
