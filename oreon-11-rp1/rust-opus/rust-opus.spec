%global source0_hash 33718946cc77d4032911d4efe03a66dbcbfbd2bb16c3da06aaeadcc637c32216
%bcond check 1
%global debug_package %{nil}
%global crate opus
%global supported_arches x86_64 s390x
Name:           rust-opus
Version:        0.4.0
Release:        1%{?dist}
Summary:        Safe Rust bindings for libopus
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/opus
Source0:        https://static.crates.io/crates/opus/opus-%{version}.crate
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
Summary:        Safe Rust bindings for libopus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifarch %{supported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifarch %{supported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-opus-devel -f %{oreon_filedir}/rust-opus-devel.list

%changelog

%autochangelog
