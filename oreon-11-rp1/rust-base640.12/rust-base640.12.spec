%global source0_hash 3441f0f7b02788e948e47f457ca01f1d7e6d92c693bc132c22b087d3141c03ff
%bcond check 0
%global debug_package %{nil}
%global crate base64
Name:           rust-base640.12
Version:        0.12.3
Release:        1%{?dist}
Summary:        encodes and decodes base64 as bytes or utf8
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/base64
Source0:        https://static.crates.io/crates/base64/base64-%{version}.crate
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
Summary:        encodes and decodes base64 as bytes or utf8
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        encodes and decodes base64 as bytes or utf8
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        encodes and decodes base64 as bytes or utf8
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-base640.12-devel -f %{oreon_filedir}/rust-base640.12-devel.list

%changelog

%autochangelog
