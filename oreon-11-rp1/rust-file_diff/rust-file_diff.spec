%global source10_hash 9d9c35115cfaceec71d04b14c8de2673dc4e010771cfe5ce02b226a7c976a279
%global source0_hash 31a7a908b8f32538a2143e59a6e4e2508988832d5d4d6f7c156b3cbc762643a5
%bcond check 1
%global debug_package %{nil}
%global crate file_diff
Name:           rust-file_diff
Version:        1.0.0
Release:        1%{?dist}
Summary:        Atomic utility for diffing files in testing
License:        BSD-3-Clause
URL:            https://crates.io/crates/file_diff
Source0:        https://static.crates.io/crates/file_diff/file_diff-%{version}.crate
Source10:       https://raw.githubusercontent.com/michel-slm/rust-file_diff/refs/heads/add-license/LICENSE
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Atomic utility for diffing files in testing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE10} .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-file_diff-devel -f %{oreon_filedir}/rust-file_diff-devel.list

%changelog

%autochangelog
