%global source0_hash 6822257f6287e2bb5838a7bd602832d6334e1f74cb7839389764aa0bff37f3d6
%global with_tests 1
Name: autowrap
Summary:        Generates Python Extension modules from [Cython] PXD files
Version: 0.26.0
Release:        1%{?dist}
License: BSD-3-Clause
URL: https://pypi.org/project/autowrap/
Source0:        https://github.com/OpenMS/autowrap/archive/refs/tags/release/%{version}/%{name}-release-%{version}.tar.gz
Patch0:  %{name}-fix_configuration_for_old_setuptools.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-autowrap = %{version}-%{release}
# /oreon:deps
%package -n       python3-autowrap+dev
Summary:        Metapackage for python3-autowrap dev extras
Requires:       python3-autowrap = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.0
Requires:       python3dist(numpy) >= 1.20
Provides:       python3dist(autowrap[dev]) = %{version}-%{release}

%description -n python3-autowrap+dev
Metapackage for python3-autowrap dev extras.

%package -n       python3-autowrap+test
Summary:        Metapackage for python3-autowrap test extras
Requires:       python3-autowrap = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.0
Requires:       python3dist(numpy) >= 1.20
Provides:       python3dist(autowrap[test]) = %{version}-%{release}

%description -n python3-autowrap+test
Metapackage for python3-autowrap test extras.

%description
This module uses the Cython "header" .pxd files to automatically generate
Cython input (.pyx) files. It does so by parsing the header files and possibly
annotations in the header files to generate correct Cython code.

%package -n python3-autowrap
Summary: Generates Python3 Extension modules from [Cython] PXD files
%py_provides python3-%{name}
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
BuildRequires: python3-Cython
Obsoletes: python2-autowrap < 0:%{version}-%{release}
# oreon:reqs
Requires:       python3dist(Cython) >= 3.1
# /oreon:reqs
%description -n python3-autowrap
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-release-%{version} -N

##Remove bundled files
rm -rf %{name}-release-%{version}/autowrap/data_files/boost

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-autowrap usr/lib/python3*/site-packages/autowrap* usr/lib64/python3*/site-packages/autowrap* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/autowrap* usr/lib64/python3*/site-packages/autowrap* usr/bin/*
%if 0%{?with_tests}
%check

export CFLAGS="-I%{_includedir}/boost"
%pytest -v -m "not network"
%endif
%files
%files -n python3-autowrap -f %{oreon_filedir}/python3-autowrap.list

%changelog

%autochangelog
