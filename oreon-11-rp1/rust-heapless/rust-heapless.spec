%global source0_hash 25ba4bd83f9415b58b4ed8dc5714c76e626a105be4646c02630ad730ad3b5aa4
%bcond check 0
%global debug_package %{nil}
%global crate heapless
Name:           rust-heapless
Version:        0.9.3
Release:        1%{?dist}
Summary:        `static` friendly data structures that don't require dynamic memory a...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/heapless
Source0:        https://static.crates.io/crates/heapless/heapless-%{version}.crate
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

%package     -n %{name}+mpmc_large-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+mpmc_large-devel

This package contains library source intended for building other packages which
use the "mpmc_large" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-critical-section-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+portable-atomic-critical-section-devel

This package contains library source intended for building other packages which
use the "portable-atomic-critical-section" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-unsafe-assume-single-core-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+portable-atomic-unsafe-assume-single-core-devel

This package contains library source intended for building other packages which
use the "portable-atomic-unsafe-assume-single-core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+ufmt-devel
Summary:        `static` friendly data structures that don't require dynamic memory a...
BuildArch:      noarch
%description -n %{name}+ufmt-devel

This package contains library source intended for building other packages which
use the "ufmt" feature of the "%{crate}" crate.

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
%files -n rust-heapless-devel -f %{oreon_filedir}/rust-heapless-devel.list

%changelog

%autochangelog
