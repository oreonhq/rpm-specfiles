%global source0_hash 790eea4361631c5e7d22598ecd5723ff611904e3344ce8720784c93e3d83d40b
%bcond check 0
%global debug_package %{nil}
%global crate critical-section
Name:           rust-critical-section
Version:        1.2.0
Release:        1%{?dist}
Summary:        Cross-platform critical section
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/critical-section
Source0:        https://static.crates.io/crates/critical-section/critical-section-%{version}.crate
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

%package     -n %{name}+restore-state-bool-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-bool-devel

This package contains library source intended for building other packages which
use the "restore-state-bool" feature of the "%{crate}" crate.

%package     -n %{name}+restore-state-none-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-none-devel

This package contains library source intended for building other packages which
use the "restore-state-none" feature of the "%{crate}" crate.

%package     -n %{name}+restore-state-u16-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-u16-devel

This package contains library source intended for building other packages which
use the "restore-state-u16" feature of the "%{crate}" crate.

%package     -n %{name}+restore-state-u32-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-u32-devel

This package contains library source intended for building other packages which
use the "restore-state-u32" feature of the "%{crate}" crate.

%package     -n %{name}+restore-state-u64-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-u64-devel

This package contains library source intended for building other packages which
use the "restore-state-u64" feature of the "%{crate}" crate.

%package     -n %{name}+restore-state-u8-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-u8-devel

This package contains library source intended for building other packages which
use the "restore-state-u8" feature of the "%{crate}" crate.

%package     -n %{name}+restore-state-usize-devel
Summary:        Cross-platform critical section
BuildArch:      noarch
%description -n %{name}+restore-state-usize-devel

This package contains library source intended for building other packages which
use the "restore-state-usize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Cross-platform critical section
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
%files -n rust-critical-section-devel -f %{oreon_filedir}/rust-critical-section-devel.list

%changelog

%autochangelog
