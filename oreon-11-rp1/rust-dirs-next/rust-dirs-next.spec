%global source0_hash b98cf8ebf19c3d1b223e151f99a4f9f0690dca41414773390fc824184ac833e1
%bcond check 0
%global debug_package %{nil}
%global crate dirs-next
Name:           rust-dirs-next
Version:        2.0.0
Release:        1%{?dist}
Summary:        A tiny low-level library that provides platform-specific standard
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dirs-next
Source0:        https://static.crates.io/crates/dirs-next/dirs-next-%{version}.crate
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
Summary:        A tiny low-level library that provides platform-specific standard
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
%files -n rust-dirs-next-devel -f %{oreon_filedir}/rust-dirs-next-devel.list

%changelog

%autochangelog
