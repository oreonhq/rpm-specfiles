%global source0_hash 974e4ed414225eb3c716985df9709f4da8d22a67a2890066bc6dfc89ad298625
Summary:        X.Org X11 ICE runtime library
Name: libICE
Version: 1.1.2
Release:        1%{?dist}
License: MIT-open-group
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.

%package devel
Summary: X.Org X11 ICE development package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The X.Org X11 ICE (Inter-Client Exchange) development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
#patch1 -p1 -b .cve-2017-2626

%build

autoreconf -v --install --force
%configure --disable-static \
	   --without-fop --without-xmlto
V=1 make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
for f in AUTHORS ChangeLog COPYING ; do
    cp -p $f ${RPM_BUILD_ROOT}%{_docdir}/%{name}/${f}
done
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libICE-devel -f %{oreon_filedir}/libICE-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-4
- Prepare for Oreon 11 (RP1)
