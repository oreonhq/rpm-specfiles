%global source0_hash c38e341c567f5f16bfa64b72fc48bba5e93873d8572522e670e6f320bbc2122f

%global _hardened_build 1

Name:		fswatch
Version:	1.17.1
Release:	6%{?dist}
Summary:	A cross-platform file change monitor
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/emcrisostomo/fswatch
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++ gcc gettext-devel
BuildRequires: make

%description
%{name} is a cross-platform file change monitor.

%package devel
Summary:	Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and headers for lib%{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static 
Static library (.a) of lib%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
%make_install
mkdir $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT%{_mandir}/man7/%{name}.7 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*

%find_lang %{name}

%check
make check

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md README.linux AUTHORS NEWS CONTRIBUTING.md ABOUT-NLS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%doc README.libfswatch.md AUTHORS.libfswatch NEWS.libfswatch
%{_libdir}/lib%{name}.so
%{_includedir}/lib%{name}/*
%{_libdir}/pkgconfig/libfswatch.pc

%files static
%{_libdir}/*.a

%changelog
%autochangelog
