%global source0_hash caf5d73b959dfbe5d6b5cd3ca8de5265c7bc58297f20560a60a1d2ba6a19991f
%bcond check 0
%global debug_package %{nil}
%global crate imagequant
Name:           rust-imagequant
Version:        4.4.1
Release:        1%{?dist}
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel.
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/imagequant
Source0:        https://static.crates.io/crates/imagequant/imagequant-%{version}.crate
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
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_internal_c_ffi-devel
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel.
BuildArch:      noarch
%description -n %{name}+_internal_c_ffi-devel

This package contains library source intended for building other packages which
use the "_internal_c_ffi" feature of the "%{crate}" crate.

%package     -n %{name}+large_palettes-devel
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel.
BuildArch:      noarch
%description -n %{name}+large_palettes-devel

This package contains library source intended for building other packages which
use the "large_palettes" feature of the "%{crate}" crate.

%package     -n %{name}+threads-devel
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel.
BuildArch:      noarch
%description -n %{name}+threads-devel

This package contains library source intended for building other packages which
use the "threads" feature of the "%{crate}" crate.

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
%files -n rust-imagequant-devel -f %{oreon_filedir}/rust-imagequant-devel.list

%changelog

%autochangelog
