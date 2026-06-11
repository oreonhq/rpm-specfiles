%global source0_hash 14975a8c1ddcc163b1afecd2207c9fd2e05b88e8a00246701fabf9dffce52ee9

Name:           kmscon
Version:        9.3.5
Release:        1%{?dist}
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
URL:            https://github.com/kmscon/kmscon/
Source0:        https://github.com/kmscon/kmscon/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  check-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  libtsm-devel >= 4.5.0
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  xsltproc
BuildRequires:  xz
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(zlib)

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
%meson -Dmulti_seat=disabled -Dvideo_fbdev=disabled

%build
%meson_build

%install
%meson_install

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

%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/kmscon-launch-gui
%{_libdir}/kmscon/mod-unifont.so
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1*
%{_mandir}/man5/kmscon.conf.5*
%{_unitdir}/kmscon.service
%{_unitdir}/kmsconvt@.service
%config /etc/kmscon/kmscon.conf.example

%files pango
%{_libdir}/kmscon/mod-pango.so

%files freetype
%{_libdir}/kmscon/mod-freetype.so

%files gl
%{_libdir}/kmscon/mod-drm3d.so
%{_libdir}/kmscon/mod-gltex.so

%changelog
* Wed Jun 10 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.3.5-1
- import for oreon 11 iso
