%global source0_hash 666e050f76eb61921e6d79e309c5833cef639de3ec1f9c35c74ebce1681f7c34
Name:             umockdev
Version:          0.19.9
Release:        1%{?dist}
Summary:        Mock hardware devices
License:          LGPL-2.1-or-later
URL:              https://github.com/martinpitt/%{name}
Source0:        https://github.com/martinpitt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libgudev1-devel
BuildRequires:  libpcap-devel
BuildRequires:  meson
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  vala
# /oreon:deps
%description
With this program and libraries you can easily create mock udev objects.
This is useful for writing tests for software which talks to
hardware devices.

%package devel
Summary: Development packages for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains the libraries to develop
using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson -Dgtk_doc=true
%meson_build
%check

export SLOW_TESTBED_FACTOR=10
%meson_test
%install
%meson_install
chrpath --delete %{buildroot}%{_bindir}/umockdev-record \
	%{buildroot}%{_bindir}/umockdev-run
chrpath --delete %{buildroot}%{_libdir}/libumockdev.so.*
chrpath --delete %{buildroot}%{_libdir}/libumockdev-preload.so.*
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/umockdev
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n umockdev-devel -f %{oreon_filedir}/umockdev-devel.list

%changelog

%autochangelog
