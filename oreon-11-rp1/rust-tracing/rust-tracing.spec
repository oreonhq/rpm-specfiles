%global source0_hash 63e71662fa4b2a2c3a26f570f037eb95bb1f85397f3cd8076caed2f026a6d100
%bcond check 0
%global debug_package %{nil}
%global crate tracing
Name:           rust-tracing
Version:        0.1.44
Release:        1%{?dist}
Summary:        Application-level tracing for Rust.
License:        MIT
URL:            https://crates.io/crates/tracing
Source0:        https://static.crates.io/crates/tracing/tracing-%{version}.crate
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
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-await-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+async-await-devel

This package contains library source intended for building other packages which
use the "async-await" feature of the "%{crate}" crate.

%package     -n %{name}+attributes-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+attributes-devel

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+log-always-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+log-always-devel

This package contains library source intended for building other packages which
use the "log-always" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_debug-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+max_level_debug-devel

This package contains library source intended for building other packages which
use the "max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_error-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+max_level_error-devel

This package contains library source intended for building other packages which
use the "max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_info-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+max_level_info-devel

This package contains library source intended for building other packages which
use the "max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_off-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+max_level_off-devel

This package contains library source intended for building other packages which
use the "max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_trace-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+max_level_trace-devel

This package contains library source intended for building other packages which
use the "max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_warn-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+max_level_warn-devel

This package contains library source intended for building other packages which
use the "max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_debug-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+release_max_level_debug-devel

This package contains library source intended for building other packages which
use the "release_max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_error-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+release_max_level_error-devel

This package contains library source intended for building other packages which
use the "release_max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_info-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+release_max_level_info-devel

This package contains library source intended for building other packages which
use the "release_max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_off-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+release_max_level_off-devel

This package contains library source intended for building other packages which
use the "release_max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_trace-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+release_max_level_trace-devel

This package contains library source intended for building other packages which
use the "release_max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_warn-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+release_max_level_warn-devel

This package contains library source intended for building other packages which
use the "release_max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-attributes-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+tracing-attributes-devel

This package contains library source intended for building other packages which
use the "tracing-attributes" feature of the "%{crate}" crate.

%package     -n %{name}+valuable-devel
Summary:        Application-level tracing for Rust.
BuildArch:      noarch
%description -n %{name}+valuable-devel

This package contains library source intended for building other packages which
use the "valuable" feature of the "%{crate}" crate.

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
%files -n rust-tracing-devel -f %{oreon_filedir}/rust-tracing-devel.list

%changelog

%autochangelog
