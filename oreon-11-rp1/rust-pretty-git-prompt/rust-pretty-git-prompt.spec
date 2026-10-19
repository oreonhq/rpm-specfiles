%global source0_hash 55640da53c949be177b33673a47b8a42360e98f5945544ff640cbfdbd09727dd
%bcond check 0
%global crate pretty-git-prompt
Name:           rust-pretty-git-prompt
Version:        0.2.2
Release:        1%{?dist}
Summary:        Your current git repository information inside a beautiful shell prompt
License:        MIT
URL:            https://crates.io/crates/pretty-git-prompt
Source0:        https://static.crates.io/crates/pretty-git-prompt/pretty-git-prompt-%{version}.crate
Patch:          pretty-git-prompt-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Your current git repository information inside a beautiful shell prompt
License:        MIT AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n pretty-git-prompt -f %{oreon_filedir}/pretty-git-prompt.list

%changelog

%autochangelog
