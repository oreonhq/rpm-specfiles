%global source0_hash 4dda5470ab2e972041804f8a5028d784bb526dff3d5a0d574221979f20ed8ac3
%bcond check 0
%global cargo_install_lib 0
%global _trunk_features -n -f native-tls
Name:           trunk
Version:        0.21.13
Release:        1%{?dist}
Summary:        Build, bundle & ship your Rust WASM application to the web
SourceLicense:  MIT OR Apache-2.0
License:        Apache-2.0 AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR MPL-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT) AND Unicode-DFS-2016
URL:            https://github.com/trunk-rs/trunk
Source0:        https://github.com/trunk-rs/trunk/archive/refs/tags/v%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1
chmod a-x vendor/bumpalo/src/lib.rs
chmod a-x vendor/zip/src/spec.rs
%oreon_vendor_cargo
%build

%cargo_build %{_trunk_features}
%{cargo_license_summary %{_trunk_features}}
%{cargo_license %{_trunk_features}} > LICENSE.dependencies
%{cargo_vendor_manifest}
%install
%cargo_install %{_trunk_features}
%oreon_autofiles main
%if %{with check}
%check

%cargo_test %{_trunk_features} -- -- --skip tools::tests::download_and_install_binaries
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
