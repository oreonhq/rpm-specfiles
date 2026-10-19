%global source0_hash 69e34f67c1ae727a75b9a75e7901738adf2779ca1024f53d280d474d1af9ff6c
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-settings-daemon
%global commit 716da6d6af0b252e2f78aba2ad72ee19ae0241e0
%global commitdatestring 2026-04-01 23:24:55 +0200
%global cosmic_minver 1.0.9
Name:           cosmic-settings-daemon
Version: 1.9.0
Release:        1%{?dist}
Summary:        Settings daemon for the COSMIC Desktop Environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-or-later AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-settings-daemon
Source0:        https://github.com/pop-os/cosmic-settings-daemon/archive/epoch-%{version}/cosmic-settings-daemon-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       acpid
Requires:       adw-gtk3-theme
Requires:       pop-sound-theme
Recommends:     geoclue2
Recommends:     playerctl
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  just
BuildRequires:  libinput-devel
BuildRequires:  libudev-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pulseaudio-utils
BuildRequires:  rustc
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-epoch-%{version} -p1 -a1
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
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%oreon_autofiles main
%if %{with check}
%check

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
