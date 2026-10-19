%global source0_hash 1130d80c7374efad55a117d715a3af9368f0fa7a2c54573afc15a188cd984837
%bcond check 1
%global debug_package %{nil}
%global crate kamadak-exif
Name:           rust-kamadak-exif
Version:        0.6.1
Release:        1%{?dist}
Summary:        Exif parsing library written in pure Rust
License:        BSD-2-Clause
URL:            https://crates.io/crates/kamadak-exif
Source0:        https://static.crates.io/crates/kamadak-exif/kamadak-exif-%{version}.crate
Patch:          0001-Remove-brittle-expected-panic-message-from-a-test.patch
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
Summary:        Exif parsing library written in pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-kamadak-exif-devel -f %{oreon_filedir}/rust-kamadak-exif-devel.list

%changelog

%autochangelog
