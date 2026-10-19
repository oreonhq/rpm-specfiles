%global source0_hash 6a6545e6262d0ed3522e13c515713718797e37ed8c672c31ad7b249f372ef108
%global pkg_name geographiclib
Name:           python-%{pkg_name}
Version:        2.1
Release:        1%{?dist}
Summary:        Python 3 implementation of geographiclib
License:        MIT
URL:            https://github.com/geographiclib/geographiclib-python
BuildArch:      noarch
Source0:        https://files.pythonhosted.org/packages/source/g/geographiclib/geographiclib-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-geographiclib = %{version}-%{release}
# /oreon:deps
%description
A translation of the GeographicLib::Geodesic class to Python.

%package -n python3-%{pkg_name}
Summary:        Python 3 implementation of %{pkg_name}
%description -n python3-%{pkg_name}
A translation of the GeographicLib::Geodesic class to Python.

%package -n mingw32-python3-%{pkg_name}
Summary:        MinGW Windows %{pkg_name} python 3 bindings
%description -n mingw32-python3-%{pkg_name}
MinGW Windows %{pkg_name} python 3 bindings.

%package -n mingw64-python3-%{pkg_name}
Summary:        MinGW Windows %{pkg_name} python 3 bindings
%description -n mingw64-python3-%{pkg_name}
MinGW Windows %{pkg_name} python 3 bindings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir geographiclib-%{version}
%oreon_prep
%build

%pyproject_wheel
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%pyproject_install
(
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
)
%mingw_debug_install_post
%oreon_autofiles main usr/lib/python3*/site-packages/geographiclib* usr/lib64/python3*/site-packages/geographiclib* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-geographiclib -f %{oreon_filedir}/python3-geographiclib.list
%files -n mingw32-python3-geographiclib -f %{oreon_filedir}/mingw32-python3-geographiclib.list
%files -n mingw64-python3-geographiclib -f %{oreon_filedir}/mingw64-python3-geographiclib.list

%changelog

%autochangelog
