%global source0_hash 6918c748c26e9c8cfe81783400be3732792a73e532d6235f40c4b332ca4fde0b
Name:           kmscon
Version:        10.0.4
Release:        1%{?dist}
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
URL:            https://github.com/kmscon/kmscon/
Source0:        https://github.com/kmscon/kmscon/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  libtsm-devel
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros
BuildRequires:  xsltproc
BuildRequires:  xz
# /oreon:deps
%description
Kmscon is a simple terminal emulator based on linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a userspace
console.

%package pango
Summary: This adds pango support to kmscon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description pango
This package provide the pango plugin to kmscon
mod-pango.so

%package freetype
Summary: This adds freetype support to kmscon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description freetype
This package provide the freetype plugin to kmscon
mod-freetype.so

%package gl
Summary: This adds opengl support to kmscon
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gl
This package provides 2 plugins for kmscon:
mod-drm3d.so
mod-gltex.so

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%conf
%meson -Dvideo_fbdev=disabled

%build

%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%post

%systemd_post kmscon.service
%systemd_post kmsconvt@.service
%preun

%systemd_preun kmscon.service
%systemd_preun kmsconvt@.service
%postun

%systemd_postun kmscon.service
%systemd_postun kmsconvt@.service
%files -f %{oreon_filedir}/main.list
%files -n kmscon-pango -f %{oreon_filedir}/kmscon-pango.list
%files -n kmscon-freetype -f %{oreon_filedir}/kmscon-freetype.list
%files -n kmscon-gl -f %{oreon_filedir}/kmscon-gl.list

%changelog

%autochangelog
