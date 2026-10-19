%global source0_hash 1e33fec9dc70408a85eca4055dca16afa82baadc2edb957e1400294b09f2ff27
%define debug_package %{nil}
ExcludeArch: %{ix86}
%bcond check 0
%global commit 04da80bb904f500ea07ec6ee4ea45d3b50adb9bb
%global commitdatestring 2026-04-07 13:36:05 -0600
%global cosmic_minver 1.0.9
Name:           cosmic-settings
Version: 1.9.0
Release:        1%{?dist}
Summary:        Settings app for the COSMIC Desktop Environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR NCSA) AND (Apache-2.0 OR MIT OR Zlib) AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Unlicense AND Zlib
URL:            https://github.com/pop-os/cosmic-settings
Source0:        https://github.com/pop-os/cosmic-settings/archive/epoch-%{version}/cosmic-settings-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       cosmic-icon-theme >= %{cosmic_minver}
Requires:       nm-connection-editor
Requires:       accountsservice
Requires:       cosmic-settings-daemon >= %{cosmic_minver}
Requires:       cosmic-randr >= %{cosmic_minver}
Requires:       gettext
Requires:       iso-codes
Requires:       NetworkManager
Requires:       ppd-service
Suggests:       tuned-ppd
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  just
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  pipewire-devel
BuildRequires:  rustc
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cosmic-settings-epoch-%{version} -p1 -a1
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
just rootdir=%{buildroot} install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicSettings.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
