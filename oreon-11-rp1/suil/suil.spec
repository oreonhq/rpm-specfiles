%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash 88ca4bcb535700ecd68a29f29db541b44913c231106d39a8e68a963665c11c68
%global source0_hash 62808916602c47d201a1ec2d246323a8048243f2bf972f859f0db1db4662ee43
%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:       suil
Version:    0.10.26
Release:        1%{?dist}
Summary:        A lightweight C library for loading and wrapping LV2 plugin UIs
License:    ISC
URL:        https://drobilla.net/software/%{name}
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg
%define __requires_exclude ^lib.*$
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  lv2-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  python-sphinxygen
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
# /oreon:deps
%description
%{name} makes it possible to load a UI of any toolkit in a host using any other
toolkit (assuming the toolkits are both supported by %{name}). Hosts do not need
to build against or link to foreign toolkit libraries to use UIs written with
that toolkit (%{name} performs its magic at runtime using dynamically
loaded modules).

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}
%description devel
This package contains the headers and development libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson -Dcocoa=disabled -Dsinglehtml=disabled
%meson_build
%install
%meson_install
install -d "%{buildroot}%{_pkgdocdir}"
mv -f "%{buildroot}%{_docdir}/%{name}-%{maj}" "%{buildroot}%{_pkgdocdir}/"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n suil-devel -f %{oreon_filedir}/suil-devel.list

%changelog

%autochangelog
