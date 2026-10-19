%global source0_hash 0bf91c779c0f6fa802ea8a18ea73142402e211073ddf6d87a11cd74ff6709a0b
%bcond check 1
%global crate szip
Name:           rust-szip
Version:        1.0.0
Release:        1%{?dist}
Summary:        Fast command line tool for snappy compression and decompression
License:        BSD-3-Clause
URL:            https://crates.io/crates/szip
Source0:        https://static.crates.io/crates/szip/szip-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Fast command line tool for snappy compression and decompression
License:        BSD-3-Clause AND MIT AND (MIT OR Apache-2.0)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
help2man --no-info --output=szip.1 target/rpm/szip
%install
%cargo_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 szip.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n szip -f %{oreon_filedir}/szip.list

%changelog

%autochangelog
