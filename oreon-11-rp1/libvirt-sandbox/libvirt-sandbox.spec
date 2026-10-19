%global source0_hash 5604cf1e8a574caca62735c513b45e083a830d3be0b684c6d05d475713ed786f
%define with_qemu 1
%define libvirt_version 1.0.2
Name: libvirt-sandbox
Version: 0.8.0
Release:        1%{?dist}
Summary:        libvirt application sandbox framework
License: LicenseRef-Callaway-LGPLv2+
URL: http://libvirt.org/
Source0:        ftp://libvirt.org/libvirt/sandbox/%{name}-%{version}.tar.gz
Requires: %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libselinux-devel
BuildRequires:  libvirt-gobject-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  xz-static
BuildRequires:  zlib-devel
BuildRequires:  zlib-static
# /oreon:deps
%package libs
Summary: libvirt application sandbox framework libraries
%if %{with_qemu}
 %ifarch %{ix86} x86_64
Requires: libvirt-daemon-kvm >= %{libvirt_version}
 %else
Requires: libvirt-daemon-qemu >= %{libvirt_version}
 %endif
%endif
Requires: libvirt-daemon-lxc >= %{libvirt_version}
%package devel
Summary: libvirt application sandbox framework development files
Requires: %{name}-libs = %{version}-%{release}
%description
This package provides a command for running applications within
a sandbox using libvirt.

%description libs
This package provides a framework for building application sandboxes
using libvirt.

%description devel
This package provides development header files and libraries for
the libvirt sandbox

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --enable-introspection
%__make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
chmod a-x examples/*.py examples/*.pl examples/*.js
%__make install  DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt-sandbox-1.0.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt-sandbox-1.0.la
%find_lang %{name}
%ldconfig_scriptlets libs
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libvirt-sandbox-libs -f %{oreon_filedir}/libvirt-sandbox-libs.list
%files -n libvirt-sandbox-devel -f %{oreon_filedir}/libvirt-sandbox-devel.list

%changelog

%autochangelog
