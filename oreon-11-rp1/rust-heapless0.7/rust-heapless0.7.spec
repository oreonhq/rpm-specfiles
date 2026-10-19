%global source0_hash cdc6457c0eb62c71aac4bc17216026d8410337c4126773b9c5daba343f17964f
%bcond check 0
%global debug_package %{nil}
%global crate heapless
Name:           rust-heapless0.7
Version:        0.7.17
Release:        1%{?dist}
Summary:        `static` friendly data structures that don't require dynamic memory a...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/heapless
Source0:        https://static.crates.io/crates/heapless/heapless-%{version}.crate
Patch:          heapless-fix-metadata.diff
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
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__trybuild-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+__trybuild-devel

This package contains library source intended for building other packages which
use the "__trybuild" feature of the "%{crate}" crate.

%package     -n %{name}+cas-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+cas-devel

This package contains library source intended for building other packages which
use the "cas" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-impl-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+defmt-impl-devel

This package contains library source intended for building other packages which
use the "defmt-impl" feature of the "%{crate}" crate.

%package     -n %{name}+mpmc_large-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+mpmc_large-devel

This package contains library source intended for building other packages which
use the "mpmc_large" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+ufmt-impl-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+ufmt-impl-devel

This package contains library source intended for building other packages which
use the "ufmt-impl" feature of the "%{crate}" crate.

%package     -n %{name}+ufmt-write-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+ufmt-write-devel

This package contains library source intended for building other packages which
use the "ufmt-write" feature of the "%{crate}" crate.

%package     -n %{name}+x86-sync-pool-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+x86-sync-pool-devel

This package contains library source intended for building other packages which
use the "x86-sync-pool" feature of the "%{crate}" crate.

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
%files -n rust-heapless0.7-devel -f %{oreon_filedir}/rust-heapless0.7-devel.list

%changelog

%autochangelog
