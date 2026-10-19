%global source0_hash be7c0abdb15cbfd29ac62573c1c82e877f9d4047ad15321e7ea97d1e43d835be
Summary:        X.Org X11 SM runtime library
Name: libSM
Version: 1.2.6
Release:        1%{?dist}
License: MIT AND MIT-open-group
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libICE-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
The X.Org X11 SM (Session Management) runtime library.

%package devel
Summary: X.Org X11 SM development package
Requires: %{name} = %{version}-%{release}
%description devel
The X.Org X11 SM (Session Management) development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -v --install --force
%configure --with-libuuid --disable-static
make %{_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libSM-devel -f %{oreon_filedir}/libSM-devel.list

%changelog

%autochangelog
