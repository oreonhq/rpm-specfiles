%global source0_hash 01a7799fd6b852db0e61728dde9a204c423b44d689dbd432522543614b490e78
%bcond check 1
%global debug_package %{nil}
%global crate crc32fast
Name:           rust-crc32fast
Version:        1.5.2
Release:        1%{?dist}
Summary:        Fast, SIMD-accelerated CRC32 (IEEE) checksum computation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crc32fast
Source0:        https://static.crates.io/crates/crc32fast/crc32fast-%{version}.crate
Patch:          crc32fast-fix-metadata.diff
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
Summary:        Fast, SIMD-accelerated CRC32 (IEEE) checksum computation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Fast, SIMD-accelerated CRC32 (IEEE) checksum computation
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast, SIMD-accelerated CRC32 (IEEE) checksum computation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-crc32fast-devel -f %{oreon_filedir}/rust-crc32fast-devel.list

%changelog

%autochangelog
