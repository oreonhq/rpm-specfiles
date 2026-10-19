%global source0_hash d2a13306348cdc3886f75c918f00e3722ec85509d0b7f286023f3929b7aa0600
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-player
%global commit 887901b323e2a8298b030bd2170e5a6421de74b3
%global commitdatestring 2026-04-07 10:33:19 -0600
%global cosmic_minver 1.0.9
Name:           cosmic-player
Version: 1.9.0
Release:        1%{?dist}
Summary:        COSMIC media player
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-player
Source0:        https://github.com/pop-os/cosmic-player/archive/epoch-%{version}/cosmic-player-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       cosmic-icon-theme >= %{cosmic_minver}
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  rustc
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
just rootdir=%{buildroot} prefix=%{_prefix} install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicPlayer.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
