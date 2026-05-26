Summary: X.Org X11 SM runtime library
Name: libSM
Version: 1.2.5
Release: 4%{?dist}
License: MIT AND MIT-open-group
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 2af9e12da5ef670dc3a7bce1895c9c0f1bfb0cb9e64e8db40fcc33f883bd20bc
%global source0_file libSM-1.2.5.tar.xz
# oreon url source checksums end

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool make
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-4
BuildRequires: libICE-devel
BuildRequires: libuuid-devel
BuildRequires: xmlto

%description
The X.Org X11 SM (Session Management) runtime library.

%package devel
Summary: X.Org X11 SM development package
Requires: %{name} = %{version}-%{release}

%description devel
The X.Org X11 SM (Session Management) development package.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libSM-1.2.5.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2af9e12da5ef670dc3a7bce1895c9c0f1bfb0cb9e64e8db40fcc33f883bd20bc" || { echo "oreon: Source0 SHA256 mismatch for libSM-1.2.5.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
autoreconf -v --install --force

%configure --with-libuuid --disable-static
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# we %%doc these ourselves, later, and only the text versions
rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libSM.so.6
%{_libdir}/libSM.so.6.*

%files devel
%dir %{_includedir}/X11/SM
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-4
- Prepare for Oreon 11 (RP1)
