%global source0_hash 127067f521d3ee467b97bcb145aeba1078e2454d448e8748eb984d5b397bde24
Summary:        X Damage extension library
Name: libXdamage
Version: 1.1.7
Release:        1%{?dist}
License: HPND-sell-variant
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXdamage runtime library.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXdamage development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -v --install --force
%configure --disable-static
make V=1 %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXdamage-devel -f %{oreon_filedir}/libXdamage-devel.list

%changelog

%autochangelog
