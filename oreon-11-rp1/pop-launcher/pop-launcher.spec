%global source0_hash ef87ccedcddb6ee0fda07ff3531a21e1c3e081173e6cb643d1ba4fa390a6d5e7
ExcludeArch: %{ix86}
%bcond check 0
%global commit 5b868510716673b31a650488401489898352e2d9
%global commitdatestring 2026-02-13 12:35:27 -0700
%global cosmic_minver 1.2.7
Name:           pop-launcher
Version: 1.2.7
Epoch: 1
Release:        1%{?dist}
Summary:        Modular IPC-based desktop launcher service
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Zlib
URL:            https://github.com/pop-os/launcher
Source0:        https://github.com/pop-os/launcher/archive/epoch-%{version}/launcher-%{version}.tar.gz
Source1:        vendor-%{version}.tar.gz
Source2:        vendor-config-%{version}.toml
Patch0: https://patch-diff.githubusercontent.com/raw/pop-os/launcher/pull/242.patch
Requires:       qalculate
Requires:       fd-find
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  mesa-libEGL-devel
BuildRequires:  rustc
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n launcher-epoch-%{version} -p1 -a1
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
export POP_LAUNCHER_LIB_DIR=/usr/libexec/pop-launcher
just build-release --offline --frozen
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
sed 's/^\([^+]*\)+.*+\([^+]*\)$/\1+\2/' -i cargo-vendor.txt
%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} lib-path=libexec install
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
