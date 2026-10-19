%global source0_hash 2e5ef9ff8428503024f84e9d0c9d8b0007dec0be42b398e5925d209ec91e2e19
ExcludeArch: %{ix86}
%bcond check 0
%global crate cosmic-term
%global build_rustflags %{?build_rustflags} --cfg=io_uring_skip_arch_check
%global commit 936e0c0628528966707174656d2c273d63465913
%global commitdatestring 2026-04-07 10:19:48 -0600
%global cosmic_minver 1.0.9
Name:           cosmic-term
Version: 1.9.0
Release:        1%{?dist}
Summary:        Terminal emulator built with alacritty and Libcosmic
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-term
Source0:        https://github.com/pop-os/cosmic-term/archive/epoch-%{version}/cosmic-term-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Requires:       cosmic-icon-theme >= %{cosmic_minver}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
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

desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicTerm.desktop
%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
