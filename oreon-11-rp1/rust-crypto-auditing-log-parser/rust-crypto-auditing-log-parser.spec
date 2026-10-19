%global source0_hash 7ac9776b77b11d77bdc6c8e14096a3058cbbfabc0725e7614cda27ba0a989bb1
%bcond check 0
%global crate crypto-auditing-log-parser
Name:           rust-crypto-auditing-log-parser
Version:        0.3.2
Release:        1%{?dist}
Summary:        Event log parser for crypto-auditing project
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/crypto-auditing-log-parser
Source0:        https://static.crates.io/crates/crypto-auditing-log-parser/crypto-auditing-log-parser-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Event log parser for crypto-auditing project
License:        GPL-3.0-or-later AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
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
%files -n crypto-auditing-log-parser -f %{oreon_filedir}/crypto-auditing-log-parser.list

%changelog

%autochangelog
