%global source0_hash 731d572b54c708f81e197a6afa8016918e2e06dfd3025e066ca642a5b8c39c8f
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        X Athena Widget Set
Name: libXaw
Version: 1.0.16
Release:        5%{?dist}
License: MIT-open-group AND X11 AND HPND AND HPND-sell-variant AND SMLNJ AND NTP
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
BuildRequires:  xmlto
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xproto) pkgconfig(xmu) pkgconfig(xt) pkgconfig(xpm)
%description devel
X.Org X11 libXaw development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure \
	    --docdir=%{_pkgdocdir} \
	    --disable-xaw8 --disable-static \
	    --disable-xaw6 \
	    --without-fop --without-xmlto
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -pm 644 COPYING README.md ChangeLog $RPM_BUILD_ROOT%{_pkgdocdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXaw-devel -f %{oreon_filedir}/libXaw-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.16-5
- Prepare for Oreon 11 (RP1)
