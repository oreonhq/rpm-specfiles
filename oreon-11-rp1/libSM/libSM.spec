Summary: X.Org X11 SM runtime library
Name: libSM
Version: 1.2.5
Release: 4%{?dist}
License: MIT AND MIT-open-group
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

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
