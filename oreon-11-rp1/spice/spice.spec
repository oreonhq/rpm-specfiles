# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0a6ec9528f05371261bbb2d46ff35e7b5c45ff89bb975a99af95a5f20ff4717d
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           spice
Version:        0.16.0
Release:        4%{?dist}
Summary:        Implements the SPICE protocol
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Patch0000:      0001-test-gst-Fix-compilation-error.patch
Patch0001:      0001-test-display-base-Fix-C-designated-initializer-for-a.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=613529
%if 0%{?rhel} && 0%{?rhel} <= 7
ExclusiveArch:  x86_64
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64
%endif

BuildRequires:  meson ninja-build
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel >= 2.22
BuildRequires:  spice-protocol >= 0.14.5
BuildRequires:  opus-devel
BuildRequires:  pixman-devel openssl-devel libjpeg-devel
BuildRequires:  libcacard-devel cyrus-sasl-devel
BuildRequires:  lz4-devel
BuildRequires:  gstreamer1-devel gstreamer1-plugins-base-devel
BuildRequires:  orc-devel
BuildRequires:  git-core
BuildRequires:  python3-pyparsing

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
%oreon_verify_sources
%autosetup -S git_am


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


%files server
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README CHANGELOG.md
%{_libdir}/libspice-server.so.1*

%files server-devel
%{_includedir}/spice-server
%{_libdir}/libspice-server.so
%{_libdir}/pkgconfig/spice-server.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-4
- Prepare for Oreon 11 (RP1)
