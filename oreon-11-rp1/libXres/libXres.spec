%global tarball libXres
#global gitdate 20130524
#global gitversion f46818496

Summary: X-Resource extension client library
Name: libXres
Version: 1.2.2
Release: 7%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: X11
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/pub/individual/lib/libXres-1.2.2.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 9a7446f3484b9b7538ac5ee30d2c1ce9e5b7fbbaf1440e02f6cca186a1fa745f
%global source0_file libXres-1.2.2.tar.xz
# oreon url source checksums end
%endif
# Fixes a bug which causes metacity 3.38.0+ to crash on startup:
# https://bugzilla.redhat.com/show_bug.cgi?id=1888993
# https://gitlab.freedesktop.org/xorg/lib/libxres/-/issues/3
# https://gitlab.freedesktop.org/xorg/lib/libxres/-/merge_requests/1

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(x11) >= 1.5.99.902

%description
X-Resource is an extension that allows a client to query
the X server about its usage of various resources. 

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXres development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXres-1.2.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9a7446f3484b9b7538ac5ee30d2c1ce9e5b7fbbaf1440e02f6cca186a1fa745f" || { echo "oreon: Source0 SHA256 mismatch for libXres-1.2.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

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
%doc AUTHORS COPYING
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0

%files devel
%{_includedir}/X11/extensions/XRes.h
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_mandir}/man3/*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-7
- Import
