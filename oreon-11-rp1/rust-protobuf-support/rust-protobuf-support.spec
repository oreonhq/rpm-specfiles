%global source0_hash 3e36c2f31e0a47f9280fb347ef5e461ffcd2c52dd520d8e216b52f93b0b0d7d6
%bcond check 1
%global debug_package %{nil}
%global crate protobuf-support
Name:           rust-protobuf-support
Version:        3.7.2
Release:        1%{?dist}
Summary:        Code supporting protobuf implementation
License:        MIT
URL:            https://crates.io/crates/protobuf-support
Source0:        https://static.crates.io/crates/protobuf-support/protobuf-support-%{version}.crate
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
Summary:        Code supporting protobuf implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-protobuf-support-devel -f %{oreon_filedir}/rust-protobuf-support-devel.list

%changelog

%autochangelog
