%global source0_hash 59307ab9e1b42ea85dbfa9f062ebcbec02b723a76034094538cd65bfbf15c725
%bcond check 0
%global crate cargo-readme
Name:           rust-cargo-readme
Version:        3.3.1
Release:        1%{?dist}
Summary:        Cargo subcommand to generate README.md content from doc comments
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-readme
Source0:        https://static.crates.io/crates/cargo-readme/cargo-readme-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Cargo subcommand to generate README.md content from doc comments
License:        MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cargo subcommand to generate README.md content from doc comments
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n cargo-readme -f %{oreon_filedir}/cargo-readme.list
%files -n rust-cargo-readme-devel -f %{oreon_filedir}/rust-cargo-readme-devel.list

%changelog

%autochangelog
