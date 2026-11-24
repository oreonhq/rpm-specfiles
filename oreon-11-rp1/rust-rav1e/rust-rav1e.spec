# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 43b6dd56e85d9483277cde964fd1bdb0428de4fec5ebba7540995639a21cb32b
%global source1_hash 205d7c4fe842d796da2bdba3d9ac1473bdd7f043903ada44ec319944f36c138b
%global source2_hash f737b20f95cfcd27f175ce7fb96caa1bb4d5cad431952584b46e513b2f2a0a3b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond check 1

%global binary_license %{shrink:
    BSD-2-Clause AND
    ISC AND
    MIT AND
    LicenseRef-BSD-2-Clause-WITH-AdditionRef-AOMPL-1.0 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}

%global crate rav1e

Name:           rust-rav1e
Version:        0.8.1
Release:        %{autorelease}
Summary:        Fastest and safest AV1 encoder
License:        BSD-2-Clause AND ISC
URL:            https://crates.io/crates/rav1e
Source0:        https://crates.io/api/v1/crates/rav1e/%{version}/download#/rav1e-%{version}.crate
Source1:        rav1e-%{version}-vendor.tar.xz
Source2:        rav1e-%{version}-Cargo.lock
Patch0:         rav1e-fix-metadata-auto.diff
Patch1:         rav1e-fix-metadata.diff
Patch2:         0001-remove-references-to-removed-built-and-profiling-cra.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cargo
BuildRequires:  rustc
BuildRequires:  cargo-c
BuildRequires:  nasm
BuildRequires:  pkgconfig(dav1d)

%description
The fastest and safest AV1 encoder.

%package     -n %{crate}
Summary:        Fastest and safest AV1 encoder
License:        %{binary_license}

%description -n %{crate}
The fastest and safest AV1 encoder.

%package     -n %{crate}-libs
Summary:        Library files for rav1e
License:        %{binary_license}

%description -n %{crate}-libs
Library files for rav1e.

%package     -n %{crate}-devel
Summary:        Development files for rav1e
License:        %{binary_license}
Requires:       %{crate}-libs%{?_isa} = %{version}-%{release}

%description -n %{crate}-devel
Development files for rav1e, including headers and pkgconfig.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -n %{crate}-%{version} -p1
cp -f %{SOURCE2} Cargo.lock
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build --features channel-api,decode_test_dav1d,unstable
cargo cbuild --release --offline --locked --features channel-api,unstable

%install
%oreon_cargo_install --features channel-api,decode_test_dav1d,unstable
cargo cinstall --release --offline --locked --destdir %{buildroot} --prefix %{_prefix} --libdir %{_libdir} --features channel-api,unstable
rm -f %{buildroot}%{_libdir}/librav1e.a

%if %{with check}
%check
%oreon_cargo_test --features channel-api,decode_test_dav1d,unstable
%endif

%files -n %{crate}
%license LICENSE
%license PATENTS
%doc README.md
%{_bindir}/rav1e
%{_bindir}/rav1e-ch

%files -n %{crate}-libs
%license LICENSE
%license PATENTS
%doc README.md
%{_libdir}/librav1e.so.0*

%files -n %{crate}-devel
%{_includedir}/rav1e/
%{_libdir}/librav1e.so
%{_libdir}/pkgconfig/rav1e.pc

%changelog
%autochangelog
