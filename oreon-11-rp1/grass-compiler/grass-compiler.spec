%global source0_hash 577858cce48440d161c6036d83dbfb3c173058f9df297977b13b8646f88a4906
%bcond check 1
%global srcname grass
Name:           grass-compiler
Version:        0.13.4
Release:        1%{?dist}
Summary:        Sass compiler written purely in Rust
License:        (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND Unicode-3.0
URL:            https://docs.rs/grass/
Source0:        https://github.com/connorskees/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Conflicts:      grass
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description
A Sass compiler written purely in Rust.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1
tomcli set Cargo.toml str workspace.resolver 2
tomcli set crates/lib/Cargo.toml del dependencies.getrandom
tomcli set crates/lib/Cargo.toml del lib.crate-type
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -D -m0755 target/release/grass %{buildroot}%{_bindir}/grass
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
