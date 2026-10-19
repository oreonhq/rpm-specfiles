%global source0_hash 31e6302e3bb753d46e83516cae55ae196fc0c309407cf11ab35cc51a4c2a4633
%bcond check 1
%global debug_package %{nil}
%global crate url
Name:           rust-url
Version:        2.5.0
Release:        1%{?dist}
Summary:        URL library for Rust, based on the WHATWG URL Standard
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/url
Source0:        https://static.crates.io/crates/url/url-%{version}.crate
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
Summary:        URL library for Rust, based on the WHATWG URL Standard
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debugger_visualizer-devel
Summary:        URL library for Rust, based on the WHATWG URL Standard
BuildArch:      noarch
%description -n %{name}+debugger_visualizer-devel

This package contains library source intended for building other packages which
use the "debugger_visualizer" feature of the "%{crate}" crate.

%package     -n %{name}+expose_internals-devel
Summary:        URL library for Rust, based on the WHATWG URL Standard
BuildArch:      noarch
%description -n %{name}+expose_internals-devel

This package contains library source intended for building other packages which
use the "expose_internals" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        URL library for Rust, based on the WHATWG URL Standard
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-url-devel -f %{oreon_filedir}/rust-url-devel.list

%changelog

%autochangelog
