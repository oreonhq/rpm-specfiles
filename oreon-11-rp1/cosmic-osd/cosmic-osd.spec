%global source0_hash 7f4e7e991f9201bacb0d0c3c47d160419de849710f16c9deb29a3aaeb82b0de3
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-osd
%global commit e2c680ed1cf7271fb4abfcffb72ebfeac0d76f09
%global commitdatestring 2026-04-06 15:04:54 -0600
%global cosmic_minver 1.0.9
Name:           cosmic-osd
Version: 1.9.0
Release:        1%{?dist}
Summary:        OSDs for the COSMIC Desktop Environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-or-later AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-osd
Source0:        https://github.com/pop-os/cosmic-osd/archive/epoch-%{version}/cosmic-osd-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       cosmic-icon-theme >= %{cosmic_minver}
Requires:       pulseaudio-utils
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  just
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  pipewire-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  rustc
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{crate}-epoch-%{version} -p1 -a1
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of %%{SOURCE2} to .cargo/config.toml
  cat %{SOURCE2} >> .cargo/config.toml
  echo "Appended %{SOURCE2} to .cargo/config.toml"
else
  # If it does not exist, append the contents of %%{SOURCE2} to .cargo/config
  cat %{SOURCE2} >> .cargo/config
  echo "Appended %{SOURCE2} to .cargo/config"
fi

%build

export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just polkit-agent-helper-1=/usr/lib/polkit-1/polkit-agent-helper-1 build-release --offline --frozen
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install
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
