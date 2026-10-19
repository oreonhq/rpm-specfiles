%global source0_hash 6e84b3f4eacbf3a1ce05eac6763b4d629d60cbc94d632e4092c54ade71f1e1a2
%bcond check 1
%global debug_package %{nil}
%global crate snafu
Name:           rust-snafu
Version:        0.8.9
Release:        1%{?dist}
Summary:        Ergonomic error handling library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/snafu
Source0:        https://static.crates.io/crates/snafu/snafu-%{version}.crate
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
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+backtraces-impl-backtrace-crate-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+backtraces-impl-backtrace-crate-devel

This package contains library source intended for building other packages which
use the "backtraces-impl-backtrace-crate" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-crate-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+futures-core-crate-devel

This package contains library source intended for building other packages which
use the "futures-core-crate" feature of the "%{crate}" crate.

%package     -n %{name}+futures-crate-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+futures-crate-devel

This package contains library source intended for building other packages which
use the "futures-crate" feature of the "%{crate}" crate.

%package     -n %{name}+guide-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+guide-devel

This package contains library source intended for building other packages which
use the "guide" feature of the "%{crate}" crate.

%package     -n %{name}+internal-dev-dependencies-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+internal-dev-dependencies-devel

This package contains library source intended for building other packages which
use the "internal-dev-dependencies" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+pin-project-devel

This package contains library source intended for building other packages which
use the "pin-project" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_61-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+rust_1_61-devel

This package contains library source intended for building other packages which
use the "rust_1_61" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_65-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+rust_1_65-devel

This package contains library source intended for building other packages which
use the "rust_1_65" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_81-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+rust_1_81-devel

This package contains library source intended for building other packages which
use the "rust_1_81" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-core-error-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+unstable-core-error-devel

This package contains library source intended for building other packages which
use the "unstable-core-error" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-provider-api-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+unstable-provider-api-devel

This package contains library source intended for building other packages which
use the "unstable-provider-api" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-try-trait-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+unstable-try-trait-devel

This package contains library source intended for building other packages which
use the "unstable-try-trait" feature of the "%{crate}" crate.

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
%files -n rust-snafu-devel -f %{oreon_filedir}/rust-snafu-devel.list

%changelog

%autochangelog
