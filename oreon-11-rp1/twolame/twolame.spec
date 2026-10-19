%global source0_hash cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d
Name:       twolame
Version:    0.4.0
Release:        9%{?dist}
Summary:        Optimized MPEG Audio Layer 2 encoding library based on tooLAME
License:    LGPL-2.1-or-later
URL:        http://www.twolame.org/
Source0:        https://downloads.sourceforge.net/twolame/%{name}-%{version}.tar.gz
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(sndfile)
# /oreon:deps
%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder. It should be able to
be used as a drop-in replacement for LAME (a MPEG Layer 3 encoder). The frontend
takes very similar command line options to LAME, and the backend library has a
very similar API to LAME.

This package contains the command line frontend.

%package libs
Summary:    TwoLAME is an optimized MPEG Audio Layer 2 encoding library based on tooLAME
%description libs
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder. It should be able to
be used as a drop-in replacement for LAME (a MPEG Layer 3 encoder). The frontend
takes very similar command line options to LAME, and the backend library has a
very similar API to LAME.

This package contains the shared library.

%package devel
Summary:    Development tools for TwoLAME applications
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and documentation needed to develop
applications with TwoLAME.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure \
    --disable-static \
    --enable-sndfile
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n twolame-libs -f %{oreon_filedir}/twolame-libs.list
%files -n twolame-devel -f %{oreon_filedir}/twolame-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-9
- Prepare for Oreon 11 (RP1)
