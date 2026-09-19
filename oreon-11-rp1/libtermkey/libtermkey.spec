%global source0_hash 6945bd3c4aaa83da83d80a045c5563da4edd7d0374c62c0d35aec09eb3014600

%global libname termkey

# Unibilium by default, otherwise ncurses
%bcond_without unibilium

Name:           lib%{libname}
Version:        0.22
Release:        12%{?dist}
Summary:        Library for easy processing of keyboard entry from terminal-based programs

License:        MIT
URL:            http://www.leonerd.org.uk/code/libtermkey
Source0:        %{url}/%{name}-%{version}.tar.gz

# Non-upstream patches
Patch0:         0001-build-take-into-account-CFLAGS-LDFLAGS-for-tests.patch
Patch1:         0002-include-stdlib.h-for-putenv.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
%if %{with unibilium}
BuildRequires:  pkgconfig(unibilium)
%else
BuildRequires:  pkgconfig(tinfo)
%endif
# For tests
BuildRequires:  %{_bindir}/prove

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

%check
CFLAGS="%{__global_cflags} -D_XOPEN_SOURCE" LDFLAGS="%{__global_ldflags}" make test VERBOSE=1

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_libdir}/pkgconfig/%{libname}.pc
%{_mandir}/man3/%{libname}_*.3*
%{_mandir}/man7/%{libname}.7*

%changelog
%autochangelog
