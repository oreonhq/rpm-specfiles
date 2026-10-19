%global source0_hash d954a5965af855ddf318556fd654c9a5a0f7901f21edc52ede4698aa6765e7b9
%bcond check 1
%ifarch %{ix86}
%global rustflags_debuginfo 1
%endif
%global crate gitui
Name:           rust-gitui
Version:        0.28.1
Release:        1%{?dist}
Summary:        Blazing fast terminal-ui for git
License:        MIT
URL:            https://crates.io/crates/gitui
Source0:        https://static.crates.io/crates/gitui/gitui-%{version}.crate
Patch:          gitui-fix-metadata.diff
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Blazing fast terminal-ui for git
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only WITH GCC-exception-2.0 AND ISC AND MPL-2.0 AND Unicode-3.0 AND Unicode-DFS-2016 AND Unlicense AND WTFPL AND Zlib AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR GPL-3.0-or-later) AND (Unlicense OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rv wix
%oreon_vendor_cargo
%build

export GITUI_RELEASE=1
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
export GITUI_RELEASE=1
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export GITUI_RELEASE=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gitui -f %{oreon_filedir}/gitui.list

%changelog

%autochangelog
