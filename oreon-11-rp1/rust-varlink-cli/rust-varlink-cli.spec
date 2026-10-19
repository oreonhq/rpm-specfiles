%global source0_hash 3506b2fc839a5c50230b44e2fbfd383a756bc9bc7cd3716b14081070cb46a5ec
%bcond check 0
%global crate varlink-cli
Name:           rust-varlink-cli
Version:        5.0.0
Release:        1%{?dist}
Summary:        Varlink command line tool
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/varlink-cli
Source0:        https://static.crates.io/crates/varlink-cli/varlink-cli-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Varlink command line tool
License:        EPL-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
Conflicts:      libvarlink-util
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
%files -n varlink-cli -f %{oreon_filedir}/varlink-cli.list

%changelog

%autochangelog
