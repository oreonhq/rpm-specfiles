%global source0_hash e309ac70c0d97e035f1e081e95655431a7bb9bca66f99a5f8186cc3fe70b4ab5
%bcond check 1
%global crate desed
Name:           rust-desed
Version:        1.2.2
Release:        1%{?dist}
Summary:        Sed script debugger
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/desed
Source0:        https://static.crates.io/crates/desed/desed-%{version}.crate
Patch:          desed-fix-metadata-auto.diff
Patch:          desed-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Sed script debugger
License:        GPL-3.0-or-later AND ISC AND MIT AND Zlib AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
Requires:       sed >= 4.6
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
%files -n desed -f %{oreon_filedir}/desed.list

%changelog

%autochangelog
