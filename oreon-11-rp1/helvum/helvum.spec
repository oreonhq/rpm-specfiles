%global source0_hash 5b46260e301d766b6999305cf8c353e01b52ca1a46918964dfd8abaf765fc647
%bcond check 0
%global cargo_install_lib 0
%global commit      980bb139e9d85d31f93045cc8a600429aa481aad
%global shortcommit %{sub %{commit} 1 7}
%global commitdate  20240829
Name:           helvum
Version:        0.5.1^%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        GTK patchbay for pipewire
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only AND (Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
URL:            https://gitlab.freedesktop.org/pipewire/helvum
Source0:        https://gitlab.freedesktop.org/pipewire/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          0001-port-to-gtk-rs-0.20-and-libadwaita-rs-0.7.patch
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n helvum-%{commit} -p1
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
sed -i -e '/dependency/d' meson.build
sed -i -e '/Cargo.lock/d' meson.build
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%meson
%meson_build
%install
%cargo_install
%meson_install
%oreon_autofiles main

%check

%if %{with check}
%cargo_test
%endif
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/org.pipewire.Helvum.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.pipewire.Helvum.metainfo.xml
appstreamcli validate --no-net \
    %{buildroot}/%{_datadir}/metainfo/org.pipewire.Helvum.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
