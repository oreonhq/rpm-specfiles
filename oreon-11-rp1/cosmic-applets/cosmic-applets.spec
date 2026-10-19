%global source0_hash f113f74cd05b179ab0478dd5876b671880914600d5df56d518f8f80c08543037
ExcludeArch: %{ix86}
%bcond check 0
%global commit f140e80bf94fc633fbcd6b3162171c8f131c3b28
%global commitdatestring 2026-04-03 19:00:36 -0400
%global cosmic_minver 1.0.9
Name:           cosmic-applets
Version: 1.9.0
Release:        1%{?dist}
Summary:        Applets for the COSMIC Desktop Environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Unlicense AND Zlib
URL:            https://github.com/pop-os/cosmic-applets
Source0:        https://github.com/pop-os/cosmic-applets/archive/epoch-%{version}/cosmic-applets-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Patch: 0001-Symlink-relative-in-justfile.patch
Requires:       cosmic-icon-theme >= %{cosmic_minver}
Requires:       cosmic-panel
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  just
BuildRequires:  libinput-devel
BuildRequires:  libudev-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pipewire-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  rustc
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cosmic-applets-epoch-%{version} -p1 -a1
if [ -f .cargo/config.toml ]; then
cat %{SOURCE2} >> .cargo/config.toml
echo "Appended %{SOURCE2} to .cargo/config.toml"
else
cat %{SOURCE2} >> .cargo/config
echo "Appended %{SOURCE2} to .cargo/config"
fi
%oreon_vendor_cargo
%build

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install
sed -e 's/"firefox"/"org.mozilla.firefox"/' -i %{buildroot}%{_datadir}/cosmic/com.system76.CosmicAppList/v1/favorites
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppList.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletA11y.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletAudio.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletBattery.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletBluetooth.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletInputSources.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletMinimize.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletNetwork.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletNotifications.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletPower.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletStatusArea.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletTiling.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletTime.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicAppletWorkspaces.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicPanelAppButton.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicPanelWorkspacesButton.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicPanelLauncherButton.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%post

%systemd_user_post com.system76.CosmicStatusNotifierWatcher.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
