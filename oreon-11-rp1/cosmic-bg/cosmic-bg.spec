%global source0_hash 848594cabc13d78fef20a907bc79aa2b132986e40bb042b9423779bfc081dcca
ExcludeArch: %{ix86}
%bcond check 0
%global commit 644993abd84bf04d7b3f2211e3656002c2a6f00b
%global commitdatestring 2026-03-13 20:45:08 +0100
%global cosmic_minver 1.0.9
Name:           cosmic-bg
Version: 1.9.0
Release:        1%{?dist}
Summary:        Background manager for the COSMIC Desktop Environment
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0
URL:            https://github.com/pop-os/cosmic-bg
Source0:        https://github.com/pop-os/cosmic-bg/archive/epoch-%{version}/cosmic-bg-%{version}.tar.gz
Requires:       cosmic-icon-theme >= %{cosmic_minver}
Requires:       desktop-backgrounds-compat
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-backgrounds-compat
BuildRequires:  desktop-file-utils
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  rustc
BuildRequires:  wayland-devel
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cosmic-bg-epoch-%{version} -p1
if [ -f .cargo/config.toml ]; then
cat %{SOURCE2} >> .cargo/config.toml
echo "Appended %{SOURCE2} to .cargo/config.toml"
else
cat %{SOURCE2} >> .cargo/config
echo "Appended %{SOURCE2} to .cargo/config"
fi
%oreon_vendor_cargo
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
if [ -f "/usr/share/backgrounds/default-dark.png" ]; then
sed -e 's|source: Path(".*"),|source: Path("/usr/share/backgrounds/default-dark.png"),|' -i %{buildroot}%{_datadir}/cosmic/com.system76.CosmicBackground/v1/all
else
sed -e 's|source: Path(".*"),|source: Path("/usr/share/backgrounds/default-dark.jxl"),|' -i %{buildroot}%{_datadir}/cosmic/com.system76.CosmicBackground/v1/all
fi
echo "true" > %{buildroot}%{_datadir}/cosmic/com.system76.CosmicBackground/v1/same-on-all
%oreon_autofiles main
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicBackground.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
