%global source0_hash 6ce1187031a365bf226a0cd146f17b4773e7ed450883f7cd502f5ecf432b5325
%global bundled_rust_deps 0
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           gnome-tour
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME Tour and Greeter
License:        (Apache-2.0 OR MIT) AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND MIT AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Unlicense OR MIT)
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        https://download.gnome.org/sources/%{name}/5%{bundled_rust_deps}/%{name}-%{version}.tar.xz
Source1:        welcome-fedora.svg
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  rustc
# /oreon:deps
%description
A guided tour and greeter for GNOME.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}
%if 0%{?bundled_rust_deps}
%else
rm -rf vendor/
%endif
%if ! 0%{?bundled_rust_deps}
%oreon_vendor_cargo
%build

%meson
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%meson_install
%find_lang gnome-tour
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Tour.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Tour.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 48.1-6
- Ship Source1 welcome-fedora.svg in tree for Fedora branding prep step

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 48.1-5
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 48.1-4
- Prepare for Oreon 11 (RP1)
%endif
