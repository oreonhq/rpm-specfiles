%global source0_hash 3d20d5497ef88037a52ff98267d066e7f11fcc5e99bbfbd58a42336193aacec3
%bcond check 0
%global debug_package %{nil}
%global crate portable-atomic
Name:           rust-portable-atomic
Version:        1.14.0
Release:        2%{?dist}
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/portable-atomic
Source0:        https://static.crates.io/crates/portable-atomic/portable-atomic-%{version}.crate
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
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+critical-section-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+critical-section-devel

This package contains library source intended for building other packages which
use the "critical-section" feature of the "%{crate}" crate.

%package     -n %{name}+disable-fiq-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+disable-fiq-devel

This package contains library source intended for building other packages which
use the "disable-fiq" feature of the "%{crate}" crate.

%package     -n %{name}+fallback-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+fallback-devel

This package contains library source intended for building other packages which
use the "fallback" feature of the "%{crate}" crate.

%package     -n %{name}+float-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+float-devel

This package contains library source intended for building other packages which
use the "float" feature of the "%{crate}" crate.

%package     -n %{name}+force-amo-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+force-amo-devel

This package contains library source intended for building other packages which
use the "force-amo" feature of the "%{crate}" crate.

%package     -n %{name}+require-cas-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+require-cas-devel

This package contains library source intended for building other packages which
use the "require-cas" feature of the "%{crate}" crate.

%package     -n %{name}+s-mode-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+s-mode-devel

This package contains library source intended for building other packages which
use the "s-mode" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-assume-privileged-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+unsafe-assume-privileged-devel

This package contains library source intended for building other packages which
use the "unsafe-assume-privileged" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-assume-single-core-devel
Summary:        Portable atomic types including support for 128-bit atomics, atomic f...
BuildArch:      noarch
%description -n %{name}+unsafe-assume-single-core-devel

This package contains library source intended for building other packages which
use the "unsafe-assume-single-core" feature of the "%{crate}" crate.

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
%files -n rust-portable-atomic-devel -f %{oreon_filedir}/rust-portable-atomic-devel.list

%changelog

%autochangelog
