%global source4_hash fc4867fa2b1aa2e9e9c4bb60f3793a19a456cdf0b55af88fec6765f3d7e07faa
%global source3_hash b079b3d6e9dd9290c9eedcb32640a0b24a1f2df07a2c2de2de85568e2ab3df01
%global source2_hash df09a5b1d682d552c54b021d3c2514d7049972e08d06a8c80f599fe75a97bc2a
%global source0_hash 05669f8e7e2d7badc545c513710f0eba09c2fbef683eb859fd79c46c355048e0
%bcond check 1
%global debug_package %{nil}
%global crate fatfs
Name:           rust-fatfs
Version:        0.3.6
Release:        1%{?dist}
Summary:        FAT filesystem library
License:        MIT
URL:            https://crates.io/crates/fatfs
Source0:        https://static.crates.io/crates/fatfs/fatfs-%{version}.crate
Source2:        https://github.com/rafalh/rust-fatfs/raw/v%{version}/resources/fat12.img
Source3:        https://github.com/rafalh/rust-fatfs/raw/v%{version}/resources/fat16.img
Source4:        https://github.com/rafalh/rust-fatfs/raw/v%{version}/resources/fat32.img
Patch:          fatfs-fix-metadata.diff
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
Summary:        FAT filesystem library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        FAT filesystem library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        FAT filesystem library
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        FAT filesystem library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
mkdir resources
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} resources/
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ifarch armv7hl %{ix86}
%cargo_test -- -- --skip test_format_512mb_512sec --skip test_format_empty_volume_label --skip test_format_volume_label_and_id
%else
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-fatfs-devel -f %{oreon_filedir}/rust-fatfs-devel.list

%changelog

%autochangelog
