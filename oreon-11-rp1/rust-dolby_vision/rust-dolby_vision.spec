# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 533d9f32336f4d03822e87fcee32277fd4a52e3f1278549bf42c8b28e3b0f798
%global source1_hash cb80dd3a7fb3217c5daa949e0487c382f441b8a60c05deec5b54f2f65bc4701f
%global source2_hash 2d408a2a1515419d075cd686be0f635d7d5f2b3f2b84f9e6744d60c25ff777e5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond check 1

%global crate dolby_vision

Name:           rust-dolby_vision
Version:        3.3.2
Release:        %{autorelease}
Summary:        Dolby Vision metadata parsing and writing

License:        MIT
URL:            https://crates.io/crates/dolby_vision
Source0:        %{crate}-%{version}.crate
Source1:        %{crate}-%{version}-vendor.tar.xz
Source2:        %{crate}-%{version}-Cargo.lock
Patch:          dolby_vision-fix-metadata.diff
Patch10:        dolby_vision-a8e639d.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cargo
BuildRequires:  rustc
BuildRequires:  cargo-c
%global _description %{expand:
Dolby Vision metadata parsing and writing.}

%description %{_description}

%package     -n libdovi
Summary:        %{summary}
License:        MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)

%description -n libdovi %{_description}

This package contains the C library.

%files       -n libdovi
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_libdir}/libdovi.so.3{,.*}

%package     -n libdovi-devel
Summary:        %{summary}
Requires:       libdovi%{?_isa} = %{version}-%{release}

%description -n libdovi-devel %{_description}

This package contains the C library development files.

%files       -n libdovi-devel
%{_libdir}/libdovi.so
%{_libdir}/pkgconfig/dovi.pc
%dir %{_includedir}/libdovi
%{_includedir}/libdovi/rpu_parser.h

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -n %{crate}-%{version} -p1
cp -f %{SOURCE2} Cargo.lock
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%oreon_cargo_build --all-features
cargo cbuild --release --offline --locked --all-features

%install
cargo cinstall --release --offline --locked --all-features --destdir %{buildroot} --prefix %{_prefix} --libdir %{_libdir}
rm -f %{buildroot}%{_libdir}/libdovi.a

%if %{with check}
%check
%oreon_cargo_test --all-features -- --skip rpu::generate::tests::config_with_frame_edits --skip xml::tests::parse
%endif

%changelog
%autochangelog
