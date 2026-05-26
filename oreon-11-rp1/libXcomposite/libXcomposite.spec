Summary: X Composite Extension library
Name: libXcomposite
Version: 0.4.6
Release: 7%{?dist}
License: MIT AND HPND-sell-variant
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 fe40bcf0ae1a09070eba24088a5eb9810efe57453779ec1e20a55080c6dc2c87
%global source0_file libXcomposite-0.4.6.tar.xz
# oreon url source checksums end

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(compositeproto) >= 0.4
BuildRequires: pkgconfig(xfixes) pkgconfig(xext)

%description
X Composite Extension library

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXcomposite development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXcomposite-0.4.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fe40bcf0ae1a09070eba24088a5eb9810efe57453779ec1e20a55080c6dc2c87" || { echo "oreon: Source0 SHA256 mismatch for libXcomposite-0.4.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING README.md ChangeLog
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0

%files devel
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%{_mandir}/man3/X?omposite*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.6-7
- Prepare for Oreon 11 (RP1)
