%global source0_hash 4c736700bbca173ca7d06738fe6f2e74c053abbea676bf083303a72984469a09
ExcludeArch: %{ix86}
%bcond check 0
%global commit 76c1fb16f78a0c1c028df953d663a7c92dc78707
%global commitdatestring 2026-04-07 10:38:49 -0600
%global cosmic_minver 1.0.9
Name:           cosmic-store
Version: 1.9.0
Release:        1%{?dist}
Summary:        App store for the COSMIC Desktop Environment
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/pop-os/cosmic-store
Source0:        https://github.com/pop-os/cosmic-store/archive/epoch-%{version}/cosmic-store-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Recommends:     PackageKit
Recommends:     flatpak
Requires:       flatpak-libs
Requires:       cosmic-icon-theme >= %{cosmic_minver}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  flatpak-devel
BuildRequires:  just
BuildRequires:  libappstream-glib
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  rustc
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cosmic-store-epoch-%{version} -p1 -a1
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
%{cargo_build} --features packagekit
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

%if %{with check}
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%{cargo_test} --features packagekit
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
