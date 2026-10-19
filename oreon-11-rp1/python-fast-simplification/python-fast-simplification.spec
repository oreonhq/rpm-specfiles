%global source0_hash ae381e7876a9ed6e33c394b8bb500fc215bff52f90b484e4b2ddef5736d94785
%bcond pyvista 0
%bcond tests 1
Name:           python-fast-simplification
Version:        0.2.0
Release:        1%{?dist}
Summary:        Wrapper around the Fast-Quadric-Mesh-Simplification library
License:        MIT
URL:            https://github.com/pyvista/fast-simplification
Source0:        https://github.com/pyvista/fast-simplification/archive/v%{version}/fast-simplification-%{version}.tar.gz
Patch:          0001-Downstream-only-do-not-override-system-compiler-flag.patch
%if %{with tests}
%endif
ExcludeArch:    %{ix86}
%global common_description %{expand:
This is a python wrapping of the Fast-Quadric-Mesh-Simplification Library
(https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification/). Having arrived
at the same problem as the original author, but needing a Python library, this
project seeks to extend the work of the original library while adding
integration to Python and the PyVista (https://github.com/pyvista/pyvista)
project.
For the full documentation visit:
https://pyvista.github.io/fast-simplification/}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(nanobind) >= 1.3.2
BuildRequires:  python3dist(scikit-build-core) >= 0.10
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-fast-simplification = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-fast-simplification
Summary:        Wrapper around the Fast-Quadric-Mesh-Simplification library
Provides:       bundled(Fast-Quadric-Mesh-Simplification) = 0^20201008git4aeffce
%description -n python3-fast-simplification %{common_description}

%prep

%autosetup -p1
%if %{without pyvista}
sed -r -i 's/^pyvista\b/# &/' requirements_test.txt
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fast-simplification usr/lib/python3*/site-packages/fast_simplification* usr/lib64/python3*/site-packages/fast_simplification* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fast_simplification* usr/lib64/python3*/site-packages/fast_simplification* usr/bin/*

%check

%if %{with tests}
%pytest -v -rs
%endif
%files
%files -n python3-fast-simplification -f %{oreon_filedir}/python3-fast-simplification.list

%changelog

%autochangelog
