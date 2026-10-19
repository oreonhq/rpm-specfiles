%global source0_hash f23e212e22ca22942cca87b18decdbce8a76d2b004c344a0789d0d26d14930d6
Name:           libcpuid
Version:        0.8.2
Release:        1%{?dist}
Summary:        Provides CPU identification for x86 and ARM
License:        BSD-2-Clause
URL:            https://github.com/anrieff/libcpuid
Source0:        https://github.com/anrieff/libcpuid/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libcpuid = %{version}-%{release}
# /oreon:deps
%description
Libcpuid provides CPU identification for the x86 (x86_64) and ARM architectures.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)

%package static
Summary:        Static development files for %{name}
Requires:       %{name}-devel%{_isa} = %{version}-%{release}
%description static
The %{name}-static package contains a library for developing applications
that need to use %{name} statically.

%package -n python3-%{name}
Summary:        Python bindings for the libcpuid library
Requires:       %{name}%{_isa} = %{version}-%{release}
%description -n python3-%{name}
The python3-%{name} package contains Python bindings for the libcpuid library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -vfi
%configure
%make_build
pushd python
%pyproject_wheel
popd
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
pushd python
%pyproject_install
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/lib/python3*/site-packages/libcpuid* usr/lib64/python3*/site-packages/libcpuid* usr/bin/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} %pytest python/tests
%files
%files -n libcpuid-devel -f %{oreon_filedir}/libcpuid-devel.list
%files -n libcpuid-static -f %{oreon_filedir}/libcpuid-static.list
%files -n python3-libcpuid -f %{oreon_filedir}/python3-libcpuid.list

%changelog

%autochangelog
