Summary: X.Org X11 libXft runtime library
Name: libXft
Version: 2.3.8
Release: 10%{?dist}
License: HPND-sell-variant
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

# Bug report: https://bugzilla.redhat.com/show_bug.cgi?id=2154735
# Upstream issue: https://gitlab.freedesktop.org/xorg/lib/libxft/-/issues/19
# Upstream fix: https://gitlab.freedesktop.org/xorg/lib/libxft/-/merge_requests/26
Patch:   fix_font_loading.patch
# oreon url source checksums begin
%global source0_sha256 5e8c3c4bc2d4c0a40aef6b4b38ed2fb74301640da29f6528154b5009b1c6dd49
%global source0_file libXft-2.3.8.tar.xz
# oreon url source checksums end

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xrender)
BuildRequires: freetype-devel >= 2.1.9-2
BuildRequires: fontconfig-devel >= 2.2-1

Requires: fontconfig >= 2.2-1

%description
X.Org X11 libXft runtime library

%package devel
Summary: X.Org X11 libXft development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXft development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXft-2.3.8.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5e8c3c4bc2d4c0a40aef6b4b38ed2fb74301640da29f6528154b5009b1c6dd49" || { echo "oreon: Source0 SHA256 mismatch for libXft-2.3.8.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
autoreconf -v --install --force

%configure --disable-static
make %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING README.md ChangeLog
%{_libdir}/libXft.so.2*

%files devel
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_mandir}/man3/Xft*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.8-10
- Prepare for Oreon 11 (RP1)
