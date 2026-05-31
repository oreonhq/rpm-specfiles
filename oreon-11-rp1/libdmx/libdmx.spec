%global source0_hash 35a4e26a8b0b2b4fe36441dca463645c3fa52d282ac3520501a38ea942cbf74f

%global tarball libdmx
#global gitdate 20130524
%global gitversion 5074d9d64

Summary: X.Org X11 DMX runtime library
Name: libdmx
Version: 1.1.5
Release: 7%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
# SPDX
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

Requires: libX11 >= 1.6.0

BuildRequires: pkgconfig(xext)
BuildRequires: autoconf automake libtool make
BuildRequires: xorg-x11-util-macros
BuildRequires: libX11-devel >= 1.6.0

%description
The X.Org X11 DMX (Distributed Multihead X) runtime library.

%package devel
Summary: X.Org X11 DMX development files
Requires: %{name} = %{version}-%{release}

%description devel
The X.Org X11 DMX (Distributed Multihead X) development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%doc COPYING
%{_libdir}/libdmx.so.1
%{_libdir}/libdmx.so.1.0.0

%files devel
%{_libdir}/libdmx.so
%{_libdir}/pkgconfig/dmx.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/dmxext.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.5-7
- Prepare for Oreon 11 (RP1)
