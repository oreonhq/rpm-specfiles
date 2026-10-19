%global source0_hash b7deadd8d3b9fdb66603e420a99fb12ca170654ee319c37a5fa8b100bf0420a5
%global somajor 1
Name:           libucontext
Version:        1.5.2
Release:        1%{?dist}
Summary:        ucontext implementation featuring glibc-compatible ABI
License:        ISC
URL:            https://github.com/kaniini/libucontext
Source0:        https://distfiles.ariadne.space/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description
libucontext is a library which provides the ucontext.h C API.
Unlike other implementations, it faithfully follows the Linux
kernel process ABI when doing context swaps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddefault_library=shared -Dexport_unprefixed=false -Dfreestanding=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libucontext-devel -f %{oreon_filedir}/libucontext-devel.list

%changelog

%autochangelog
