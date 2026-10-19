%global source0_hash 3763264f6b73151db08c50ff20d7d8a0b8796e021cdea7ceedad07b80155fa0e
%bcond check 0
%global debug_package %{nil}
%global crate spin
Name:           rust-spin0.9
Version:        0.9.9
Release:        1%{?dist}
Summary:        Spin-based synchronization primitives
License:        MIT
URL:            https://crates.io/crates/spin
Source0:        https://static.crates.io/crates/spin/spin-%{version}.crate
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
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+barrier-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+barrier-devel

This package contains library source intended for building other packages which
use the "barrier" feature of the "%{crate}" crate.

%package     -n %{name}+fair_mutex-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+fair_mutex-devel

This package contains library source intended for building other packages which
use the "fair_mutex" feature of the "%{crate}" crate.

%package     -n %{name}+lazy-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+lazy-devel

This package contains library source intended for building other packages which
use the "lazy" feature of the "%{crate}" crate.

%package     -n %{name}+lock_api-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+lock_api-devel

This package contains library source intended for building other packages which
use the "lock_api" feature of the "%{crate}" crate.

%package     -n %{name}+lock_api_crate-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+lock_api_crate-devel

This package contains library source intended for building other packages which
use the "lock_api_crate" feature of the "%{crate}" crate.

%package     -n %{name}+mutex-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+mutex-devel

This package contains library source intended for building other packages which
use the "mutex" feature of the "%{crate}" crate.

%package     -n %{name}+once-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+once-devel

This package contains library source intended for building other packages which
use the "once" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+portable_atomic-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+portable_atomic-devel

This package contains library source intended for building other packages which
use the "portable_atomic" feature of the "%{crate}" crate.

%package     -n %{name}+rwlock-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+rwlock-devel

This package contains library source intended for building other packages which
use the "rwlock" feature of the "%{crate}" crate.

%package     -n %{name}+spin_mutex-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+spin_mutex-devel

This package contains library source intended for building other packages which
use the "spin_mutex" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+ticket_mutex-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+ticket_mutex-devel

This package contains library source intended for building other packages which
use the "ticket_mutex" feature of the "%{crate}" crate.

%package     -n %{name}+use_ticket_mutex-devel
Summary:        Spin-based synchronization primitives
BuildArch:      noarch
%description -n %{name}+use_ticket_mutex-devel

This package contains library source intended for building other packages which
use the "use_ticket_mutex" feature of the "%{crate}" crate.

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
%files -n rust-spin0.9-devel -f %{oreon_filedir}/rust-spin0.9-devel.list

%changelog

%autochangelog
