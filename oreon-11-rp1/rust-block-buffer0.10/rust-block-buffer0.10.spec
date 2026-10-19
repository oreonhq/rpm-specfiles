%global source0_hash 3078c7629b62d3f0439517fa394996acacc5cbc91c5a20d8c658e77abd503a71
%bcond check 0
%global debug_package %{nil}
%global crate block-buffer
Name:           rust-block-buffer0.10
Version:        0.10.4
Release:        1%{?dist}
Summary:        Buffer type for block processing of data
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/block-buffer
Source0:        https://static.crates.io/crates/block-buffer/block-buffer-%{version}.crate
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
Summary:        Buffer type for block processing of data
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
%files -n rust-block-buffer0.10-devel -f %{oreon_filedir}/rust-block-buffer0.10-devel.list

%changelog

%autochangelog
