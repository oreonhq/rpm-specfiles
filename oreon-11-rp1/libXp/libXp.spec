# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 1f19e3b8e82a34a8fd9889a7d9af0abe8588cb03fb57c37c569634cf3b9df1a4
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# NOTE: This library has been deprecated in RHEL and Fedora for some
# time now.  While we have removed the word "deprecated" from the package
# name in modular X, the library does remain deprecated and will be
# removed from a future OS release at some point.  Developers should
# refrain from using this library in new software, and should migrate
# software which currently uses libXp to another printing interface such
# as gnome-print.  We may decide to stop shipping the development headers
# prior to removing libXp from the OS.

Summary: X.Org X11 libXp runtime library
Name: libXp
Version: 1.0.4
Release: 10%{?dist}
License: X11 AND X11-distribute-modifications-variant
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXau-devel
BuildRequires: libtool automake autoconf gettext

Patch0: add-proto-files.patch

%description
X.Org X11 libXp runtime library

%package devel
Summary: X.Org X11 libXp development package
Requires: libXau-devel pkgconfig
Requires: %{name} = %{version}-%{release}

# needed by xp.pc
BuildRequires: xorg-x11-proto-devel

%description devel
X.Org X11 libXp development package

%prep
%oreon_verify_sources
%setup -q
%patch -P0 -p1 -b .add-proto-files

%build
CPPFLAGS="$CPPFLAGS -I$RPM_BUILD_ROOT%{_includedir}"
export CPPFLAGS

autoreconf -v --install

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# Don't encourage people to use the deprecated Xprint APIs.
rm -rf $RPM_BUILD_ROOT%{_mandir}

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXp.so.6
%{_libdir}/libXp.so.6.2.0

%files devel
%{_includedir}/X11/extensions/Print.h
%{_includedir}/X11/extensions/Printstr.h
%{_libdir}/pkgconfig/printproto.pc
%{_libdir}/libXp.so
%{_libdir}/pkgconfig/xp.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-10
- Import
