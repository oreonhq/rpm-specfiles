%global source0_hash 3e64fa4cd1a742ae34b6f6d8e6d9614a2d3eab88a1b0071c11ab53617eb214c2
%bcond_without check
%bcond bundled_rust_deps %{defined rhel}
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           snapshot
Version:        51.0
Release:        1%{?dist}
Summary:        Take pictures and videos
License:        %{shrink:
    GPL-3.0-or-later AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MPL-2.0 OR LGPL-2.1-or-later) AND
    (Unlicense OR MIT) AND
    (Zlib OR Apache-2.0 OR MIT)
}
URL:            https://gitlab.gnome.org/GNOME/snapshot
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Patch:          0001-Remove-clippy-tests-linters-should-not-be-run-downst.patch
ExcludeArch:    %{ix86}
Requires:       gstreamer1-plugins-bad-free%{_isa}
Requires:       gstreamer1-plugin-gtk4%{_isa}
Requires:       glycin-loaders >= 1.1
Requires:       hicolor-icon-theme
Provides:       bundled(crate(aperture)) = 0.12.0
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  rustc
# /oreon:deps
%description
Take pictures and videos on your computer, tablet, or phone.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n snapshot-%{tarball_version}
%if %{with bundled_rust_deps}
%else
rm -rf vendor
%endif
%if %{without bundled_rust_deps}
%oreon_vendor_cargo
%build

%meson
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%meson_install
%find_lang snapshot --with-gnome
%oreon_autofiles main
%if %{with check}
%check

%meson_test \
%ifarch riscv64
    --timeout-multiplier 10 \
%endif
    %{nil}
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Snapshot.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Snapshot.desktop
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
%endif
