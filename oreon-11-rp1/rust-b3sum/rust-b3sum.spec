%global source0_hash 549398f8f677d3d3700b9ee4eeaf6d9c1fad88eea324f0633523a315fbcd8dff
%bcond check 1
%global crate b3sum
Name:           rust-b3sum
Version:        1.8.3
Release:        1%{?dist}
Summary:        Command line implementation of the BLAKE3 hash function
License:        Apache-2.0 OR Apache-2.0 WITH LLVM-exception
URL:            https://crates.io/crates/b3sum
Source0:        https://static.crates.io/crates/b3sum/b3sum-%{version}.crate
Patch:          b3sum-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command line implementation of the BLAKE3 hash function
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                BSD-2-Clause AND
                MIT AND
                (MIT-0 OR Apache-2.0)
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
help2man --no-info --output=b3sum.1 target/rpm/b3sum
%install
%cargo_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 b3sum.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n b3sum -f %{oreon_filedir}/b3sum.list

%changelog

%autochangelog
