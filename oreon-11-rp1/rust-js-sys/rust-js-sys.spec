%global source0_hash 53b44bfcdb3f8d5837a46dae1ca9660a837176eee74a28b229bc626816589102
%bcond check 0
%global debug_package %{nil}
%global crate js-sys
Name:           rust-js-sys
Version:        0.3.103
Release:        1%{?dist}
Summary:        Bindings for all JS global objects and functions in all JS environmen...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/js-sys
Source0:        https://static.crates.io/crates/js-sys/js-sys-%{version}.crate
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
Summary:        Bindings for all JS global objects and functions in all JS environmen...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-03-stream-devel
Summary:        Bindings for all JS global objects and functions in all JS environmen...
BuildArch:      noarch
%description -n %{name}+futures-core-03-stream-devel

This package contains library source intended for building other packages which
use the "futures-core-03-stream" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Bindings for all JS global objects and functions in all JS environmen...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-eval-devel
Summary:        Bindings for all JS global objects and functions in all JS environmen...
BuildArch:      noarch
%description -n %{name}+unsafe-eval-devel

This package contains library source intended for building other packages which
use the "unsafe-eval" feature of the "%{crate}" crate.

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
%files -n rust-js-sys-devel -f %{oreon_filedir}/rust-js-sys-devel.list

%changelog

%autochangelog
