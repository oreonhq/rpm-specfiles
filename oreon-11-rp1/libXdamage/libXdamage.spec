%global source0_hash 52733c1f5262fca35f64e7d5060c6fcd81a880ba8e1e65c9621cf0727afb5d11

Summary: X Damage extension library
Name: libXdamage
Version: 1.1.6
Release: 7%{?dist}
License: HPND-sell-variant
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(damageproto) >= 1.1.0

%description
X.Org X11 libXdamage runtime library.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXdamage development package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING README.md ChangeLog
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.1.0

%files devel
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-7
- Prepare for Oreon 11 (RP1)
