%global source0_hash 8f3d9ec4a8fcfa57425621eb21dc7c6cefc2f24b2a93d28db0ace9d1eab627c6

%global libname tickit
%global libtickit_ver  v0.4

# Unibilium by default, otherwise ncurses
%bcond_without unibilium

Name:           lib%{libname}
Version:        0.4.5
Release:        3%{?dist}
Summary:        Terminal Interface Construction Kit

License:        MIT
URL:            https://launchpad.net/%{name}
Source0:        %{url}/trunk/%{libtickit_ver}/+download/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::Color)
BuildRequires:  perl(Convert::Color::XTerm)
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(termkey)
%if %{with unibilium}
BuildRequires:  pkgconfig(unibilium) >= 1.1.0
%else
BuildRequires:  ncurses-devel
%endif
# Tests
BuildRequires:  %{_bindir}/prove

%description
This library provides an abstracted mechanism for building interactive
full-screen terminal programs. It provides a full set of output drawing
functions, and handles keyboard and mouse input events.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtermkey-devel%{?_isa}
%if %{with unibilium}
Requires:       unibilium-devel%{?_isa}
%endif

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
rm -f src/linechars.inc src/xterm-palette.inc

%build
CFLAGS="%{__global_cflags}" LDFLAGS="%{__global_ldflags}" %{make_build} VERBOSE=1

%install
%{make_install} PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
CFLAGS="%{__global_cflags} -D_XOPEN_SOURCE" LDFLAGS="%{__global_ldflags}" make test VERBOSE=1
make examples

%files
%license LICENSE
%doc CHANGES examples README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_includedir}/%{libname}-*.h
%{_libdir}/pkgconfig/%{libname}.pc
%{_mandir}/man3/%{libname}_*.3*
%{_mandir}/man7/%{libname}.7*
%{_mandir}/man7/%{libname}_*.7*

%changelog
%autochangelog
