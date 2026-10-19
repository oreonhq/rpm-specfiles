%global source0_hash 56ecb380d74bf74caba193d9e8ad6b0c85ccf9eeb461bc9731c2b8636e1f1492
Name:	 libunity
Summary:        Library for integrating with Unity and Plasma
Version: 7.1.4
Release:        1%{?dist}
License: GPL-3.0-only
URL:	 https://launchpad.net/libunity
Source0:        https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/libunity/%{version}+19.04.20190319-0ubuntu1/libunity_%{version}+19.04.20190319.orig.tar.gz
Patch0:  https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/libunity/%{version}+19.04.20190319-0ubuntu1/libunity_%{version}+19.04.20190319-0ubuntu1.diff.gz
Patch0001:  https://launchpadlibrarian.net/443817430/0001-Fix-FTB-with-recent-vala-requiring-non-public-abstra.patch
Patch2:  libunity-7.1.4-vala-053.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dee-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  vala
# /oreon:deps
%description
A library for instrumenting and integrating with all aspects of the Unity
shell and providing some integration features with Plasma.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n python3-libunity
Summary: Python3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-gobject-base
%description -n python3-libunity
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p1
%patch -P1 -p1 -b .0001
%patch -P2 -p1 -b .vala_053

%build

NOCONFIGURE=1 \
./autogen.sh
PYTHON=%{__python3}
export PYTHON
%configure \
  --disable-schemas-compile \
  --disable-silent-rules \
  --disable-static
%make_build
%install
%make_install
rm -fv \
  %{buildroot}%{_libdir}/lib*.la \
  %{buildroot}%{_libdir}/libunity/*.{la,so}
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/gi/overrides/
%ldconfig_post
%oreon_autofiles python3-libunity usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%postun

%{?ldconfig}
%files -f %{oreon_filedir}/main.list
%files -n libunity-devel -f %{oreon_filedir}/libunity-devel.list
%files -n python3-libunity -f %{oreon_filedir}/python3-libunity.list

%changelog

%autochangelog
