%global source0_hash bd492b6e203b10b30857778f4dd26f688426cd352937bd7779ee245139bafa2b
%global _hardened_build 1
Name:		fswatch
Version:	1.17.1
Release:        1%{?dist}
Summary:        A cross-platform file change monitor
License:	GPL-3.0-or-later
URL:		https://github.com/emcrisostomo/fswatch
Source0:        https://github.com/emcrisostomo/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n fswatch-devel -f %{oreon_filedir}/fswatch-devel.list
%files -n fswatch-static -f %{oreon_filedir}/fswatch-static.list

%changelog

%autochangelog
