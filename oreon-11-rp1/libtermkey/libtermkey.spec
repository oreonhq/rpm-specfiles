%global source0_hash 6945bd3c4aaa83da83d80a045c5563da4edd7d0374c62c0d35aec09eb3014600
%global libname termkey
%bcond_without unibilium
Name:           lib%{libname}
Version:        0.22
Release:        1%{?dist}
Summary:        Library for easy processing of keyboard entry from terminal-based programs
License:        MIT
URL:            http://www.leonerd.org.uk/code/libtermkey
Source0:        http://www.leonerd.org.uk/code/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-build-take-into-account-CFLAGS-LDFLAGS-for-tests.patch
Patch1:         0002-include-stdlib.h-for-putenv.patch
%if %{with unibilium}
%else
%endif
# oreon:deps
BuildRequires:  /usr/bin/prove
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(unibilium)
# /oreon:deps
%description
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognise special keys, UTF-8
combining, and so on, with a simple interface.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# no need for demos
sed -i -e '/^all:/s/$(DEMOS)//' Makefile

%build

CFLAGS="%{__global_cflags}" LDFLAGS="%{__global_ldflags}" %make_build VERBOSE=1
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

CFLAGS="%{__global_cflags} -D_XOPEN_SOURCE" LDFLAGS="%{__global_ldflags}" make test VERBOSE=1
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libtermkey-devel -f %{oreon_filedir}/libtermkey-devel.list

%changelog

%autochangelog
