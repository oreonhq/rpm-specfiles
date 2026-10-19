%global source0_hash fde9402dd4cfe79da71e2d96bb980afc5e6ff4f8a7d74c159e1966afb2b2c2c0
%global tarball libXcursor
%global gitversion 8f677eaea
Summary:        Cursor management library
Name: libXcursor
Version: 1.2.3
Release:        1%{?dist}
License: HPND-sell-variant
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source2:    make-git-snapshot.sh
Source3:    commitid
%else
%endif
Source1: index.theme
Requires: libX11 >= 1.5.99.902
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrender-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
This is  a simple library designed to help locate and load cursors.
Cursors can be loaded from files or memory. A library of common cursors
exists which map to the standard X cursor names.Cursors can exist in
several sizes and the library automatically picks the best size.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
libXcursor development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}
iconv --from=ISO-8859-2 --to=UTF-8 COPYING > COPYING.new && \
touch -r COPYING COPYING.new && \
mv COPYING.new COPYING

# Disable static library creation by default.
%define with_static 0

%build

autoreconf -v --install --force
%configure \
%if ! %{with_static}
 --disable-static
%endif
make V=1 %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/default
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/default/index.theme
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXcursor-devel -f %{oreon_filedir}/libXcursor-devel.list

%changelog

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-5
- Drop commented man3x line (rpmbuild expands macros in comments)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-4
- Prepare for Oreon 11 (RP1)
