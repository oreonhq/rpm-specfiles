%global source0_hash b021dc6dbc72a077777a9fe846072eb790fa1759995ef7c6b7298eeab35adafc
%global source1_hash 5a2180200b26b8351e640340718f920da4b0e1e9bcf62ae2dd2fa21350938daa
%bcond check 1
%global crate askalono-cli
Name:           rust-askalono-cli
Version:        0.5.0
Release:        1%{?dist}
Summary:        Tool to detect the contents of license files
License:        Apache-2.0 AND CC0-1.0
URL:            https://crates.io/crates/askalono-cli
Source0:        https://static.crates.io/crates/askalono-cli/askalono-cli-%{version}.crate
Source1:        askalono-cache-3.22.bin.zstd
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool to detect the contents of license files
License:        Apache-2.0 AND CC0-1.0 AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
Provides:       bundled(spdx-license-list-data) = 3.22
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} embedded-cache.bin.zstd
%oreon_vendor_cargo
%build

%cargo_build -f diagnostics
%{cargo_license_summary -f diagnostics}
%{cargo_license -f diagnostics} > LICENSE.dependencies
%install
%cargo_install -f diagnostics
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -f diagnostics
%endif
%files -f %{oreon_filedir}/main.list
%files -n askalono-cli -f %{oreon_filedir}/askalono-cli.list

%changelog

%autochangelog
