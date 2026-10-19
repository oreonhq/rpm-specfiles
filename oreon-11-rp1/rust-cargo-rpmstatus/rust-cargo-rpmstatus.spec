%global source0_hash 19004a335a8c05eed77531466b740da3c67e30ce6bbc3a576560bbb97288bdf0
%bcond check 1
%global crate cargo-rpmstatus
Name:           rust-cargo-rpmstatus
Version:        0.2.4
Release:        1%{?dist}
Summary:        Cargo-tree for RPM packaging
License:        (MIT OR Apache-2.0) AND GPL-3.0-or-later
URL:            https://crates.io/crates/cargo-rpmstatus
Source0:        https://static.crates.io/crates/cargo-rpmstatus/cargo-rpmstatus-%{version}.crate
Patch:          cargo-rpmstatus-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Cargo-tree for RPM packaging
License:       (MIT OR Apache-2.0) AND GPL-3.0-or-later AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND bzip2-1.0.6
Requires:       rust
Requires:       cargo
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
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{crate}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- -- --skip db::tests::online_check_version_reqs
%endif
%files -f %{oreon_filedir}/main.list
%files -n cargo-rpmstatus -f %{oreon_filedir}/cargo-rpmstatus.list

%changelog

%autochangelog
