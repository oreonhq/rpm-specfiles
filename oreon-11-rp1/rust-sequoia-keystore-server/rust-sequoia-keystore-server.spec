%global source2_hash 7a9b2b9d24e0844aaef27c4c47ecbe65437fefac6da5753db029e65efaefc6c1
%global source0_hash 5b2105d5a55a30634595c18538959651153de678e0ea64ed495c5b1e79ffae80
%bcond check 1
%global crate sequoia-keystore-server
Name:           rust-sequoia-keystore-server
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sequoia keystore daemon
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-keystore-server
Source0:        https://static.crates.io/crates/sequoia-keystore-server/sequoia-keystore-server-%{version}.crate
Source2:        https://gitlab.com/sequoia-pgp/sequoia-keystore/-/raw/server/v0.2.0/LICENSE.txt
Patch:          sequoia-keystore-server-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Sequoia keystore daemon
License:        %{shrink:
    LGPL-2.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}/%{_libexecdir}
mv %{buildroot}/%{_bindir}/sequoia-keystore %{buildroot}/%{_libexecdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-keystore-server -f %{oreon_filedir}/sequoia-keystore-server.list

%changelog

%autochangelog
