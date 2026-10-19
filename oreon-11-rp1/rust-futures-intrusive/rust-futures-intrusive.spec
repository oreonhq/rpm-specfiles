%global source0_hash 1d930c203dd0b6ff06e0201a4a2fe9149b43c684fd4420555b26d21b1a02956f
%bcond check 1
%global debug_package %{nil}
%global crate futures-intrusive
Name:           rust-futures-intrusive
Version:        0.5.0
Release:        1%{?dist}
Summary:        Futures based on intrusive data structures - for std and no-std environments
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-intrusive
Source0:        https://static.crates.io/crates/futures-intrusive/futures-intrusive-%{version}.crate
Patch:          futures-intrusive-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Futures based on intrusive data structures - for std and no-std environments
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Futures based on intrusive data structures - for std and no-std environments
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Futures based on intrusive data structures - for std and no-std environments
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Futures based on intrusive data structures - for std and no-std environments
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml del dev-dependencies.criterion
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- %{shrink:
    --skip if_std::mpmc_channel_tests::try_send_unbuffered_panics
    --skip local_mpmc_channel_tests::try_send_unbuffered_panics
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-futures-intrusive-devel -f %{oreon_filedir}/rust-futures-intrusive-devel.list

%changelog

%autochangelog
