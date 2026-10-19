%global source0_hash 227d2865b4e318a251257ec3718542c4ad9f9afbd6d7deb052ae7942a0d52f97
%bcond check 1
%global crate elfcat
Name:           rust-elfcat
Version:        0.1.10
Release:        1%{?dist}
Summary:        ELF visualizer. Generates HTML files from ELF binaries
License:        Zlib
URL:            https://crates.io/crates/elfcat
Source0:        https://static.crates.io/crates/elfcat/elfcat-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        ELF visualizer. Generates HTML files from ELF binaries
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n elfcat -f %{oreon_filedir}/elfcat.list

%changelog

%autochangelog
