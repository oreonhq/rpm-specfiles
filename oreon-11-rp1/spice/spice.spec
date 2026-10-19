%global source0_hash 0a6ec9528f05371261bbb2d46ff35e7b5c45ff89bb975a99af95a5f20ff4717d
Name:           spice
Version:        0.16.0
Release:        4%{?dist}
Summary:        Implements the SPICE protocol
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Patch0000:      0001-test-gst-Fix-compilation-error.patch
Patch0001:      0001-test-display-base-Fix-C-designated-initializer-for-a.patch
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libcacard-devel
BuildRequires:  libjpeg-devel
BuildRequires:  lz4-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  orc-devel
BuildRequires:  pixman-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-pyparsing
BuildRequires:  spice-protocol
# /oreon:deps
%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

%package server
Summary:        Implements the server side of the SPICE protocol
Obsoletes:      spice-client < %{version}-%{release}
%description server
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the run-time libraries for any application that wishes
to be a SPICE server.

%package server-devel
Summary:        Header files, libraries and development documentation for spice-server
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description server-devel
This package contains the header files, static libraries and development
documentation for spice-server. If you like to develop programs
using spice-server, you will need to install spice-server-devel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
	-Dopus=enabled \
	-Dsmartcard=enabled \
	-Dlz4=true \
	-Dgstreamer=1.0
%meson_build
%check

%meson_test
%install
%meson_install
%ldconfig_scriptlets server
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n spice-server -f %{oreon_filedir}/spice-server.list
%files -n spice-server-devel -f %{oreon_filedir}/spice-server-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-4
- Prepare for Oreon 11 (RP1)
