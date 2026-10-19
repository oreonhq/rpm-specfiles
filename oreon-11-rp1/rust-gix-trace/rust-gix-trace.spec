%global source0_hash be3eb81d9dc914335923e50d52829c551feefd6a72d176c4130c546b67a60814
%bcond check 0
%global debug_package %{nil}
%global crate gix-trace
Name:           rust-gix-trace
Version:        0.1.21
Release:        1%{?dist}
Summary:        A crate to provide minimal `tracing` support that can be turned off t...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-trace
Source0:        https://static.crates.io/crates/gix-trace/gix-trace-%{version}.crate
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
Summary:        A crate to provide minimal `tracing` support that can be turned off t...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate to provide minimal `tracing` support that can be turned off t...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        A crate to provide minimal `tracing` support that can be turned off t...
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-detail-devel
Summary:        A crate to provide minimal `tracing` support that can be turned off t...
BuildArch:      noarch
%description -n %{name}+tracing-detail-devel

This package contains library source intended for building other packages which
use the "tracing-detail" feature of the "%{crate}" crate.

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
%files -n rust-gix-trace-devel -f %{oreon_filedir}/rust-gix-trace-devel.list

%changelog

%autochangelog
