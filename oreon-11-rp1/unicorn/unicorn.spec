%global source0_hash ea8863f095a0136388694e5a6063afd9bb7650e30243dd6251af59c5ce5601f4
Name:           unicorn
Version:        2.1.4
Release:        1%{?dist}
Summary:        Lightweight multi-platform, multi-architecture CPU emulator framework
License:        GPL-2.0-only AND LGPL-2.1-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.unicorn-engine.org/
Source0:        https://github.com/unicorn-engine/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        COPYING
Provides: bundled(qemu) = 2.2.1
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-unicorn = %{version}-%{release}
# /oreon:deps
%package -n       python3-unicorn+test
Summary:        Metapackage for python3-unicorn test extras
Requires:       python3-unicorn = %{version}-%{release}
Requires:       python3dist(capstone) == 6.0.0a2
Requires:       python3dist(capstone) == 5.0.1
Provides:       python3dist(unicorn[test]) = %{version}-%{release}

%description -n python3-unicorn+test
Metapackage for python3-unicorn test extras.

%description

%package devel
Summary:        Files needed to develop applications using unicorn
Requires:       %{name} = %{version}-%{release}
%description devel
This package provides the libraries, include files, and other resources
needed for developing applications using unicorn.

%package -n python3-unicorn
Summary:        Files needed to develop applications using unicorn
Requires:       %{name} = %{version}-%{release}
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-unicorn
The unicorn-python3 package contains python3 bindings for unicorn.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

pushd src
%cmake
%cmake_build
popd
%pyproject_wheel
%install
pushd src
%cmake_install
popd
%pyproject_install
rm $RPM_BUILD_ROOT%{_libdir}/libunicorn.a
rm $RPM_BUILD_ROOT%{_libdir}/unicorn.o
%oreon_autofiles python3-unicorn usr/lib/python3*/site-packages/unicorn* usr/lib64/python3*/site-packages/unicorn* usr/bin/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/unicorn* usr/lib64/python3*/site-packages/unicorn* usr/bin/*

%check

%files
%files -n unicorn-devel -f %{oreon_filedir}/unicorn-devel.list
%files -n python3-unicorn -f %{oreon_filedir}/python3-unicorn.list

%changelog

%autochangelog
