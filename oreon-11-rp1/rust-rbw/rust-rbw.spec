%global source0_hash b55a65dc2cf3f2e849f50bf38167b4303cfaf9e962586d67be8d351ec3d99cde
%bcond check 1
%global cargo_install_lib 0
%global crate rbw
Name:           rust-rbw
Version:        1.13.2
Release:        1%{?dist}
Summary:        Unofficial Bitwarden CLI
License:        MIT
URL:            https://crates.io/crates/rbw
Source0:        https://static.crates.io/crates/rbw/rbw-%{version}.crate
Patch:          rbw-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Unofficial Bitwarden CLI
License:        %{shrink:
                MIT
                AND (MIT OR Apache-2.0) AND Unicode-DFS-2016
                AND Apache-2.0
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR ISC OR MIT)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND BSD-3-Clause
                AND ISC AND OpenSSL
                AND (MIT OR Apache-2.0 OR Zlib)
                AND MPL-2.0
                AND (Unlicense OR MIT)
		}
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
%files -n rbw -f %{oreon_filedir}/rbw.list

%changelog

%autochangelog
