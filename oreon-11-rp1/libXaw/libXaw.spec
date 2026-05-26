%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: X Athena Widget Set
Name: libXaw
Version: 1.0.16
Release: 5%{?dist}
License: MIT-open-group AND X11 AND HPND AND HPND-sell-variant AND SMLNJ AND NTP
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 731d572b54c708f81e197a6afa8016918e2e06dfd3025e066ca642a5b8c39c8f
%global source0_file libXaw-1.0.16.tar.xz
# oreon url source checksums end

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xproto) pkgconfig(x11) pkgconfig(xt)
BuildRequires: pkgconfig(xmu) pkgconfig(xpm) pkgconfig(xext)
BuildRequires: xorg-x11-util-macros xmlto lynx

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXaw-1.0.16.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "731d572b54c708f81e197a6afa8016918e2e06dfd3025e066ca642a5b8c39c8f" || { echo "oreon: Source0 SHA256 mismatch for libXaw-1.0.16.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/COPYING
%{_pkgdocdir}/README.md
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0

%files devel
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*.h
# FIXME:  Is this C file really supposed to be here?
%{_includedir}/X11/Xaw/Template.c
%{_libdir}/libXaw.so
%{_libdir}/libXaw7.so
%{_libdir}/pkgconfig/xaw7.pc
%{_mandir}/man3/*.3*
%{_pkgdocdir}/*.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.16-5
- Prepare for Oreon 11 (RP1)
