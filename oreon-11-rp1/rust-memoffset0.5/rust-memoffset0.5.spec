%global source0_hash 043175f069eda7b85febe4a74abbaeff828d9f8b448515d3151a14a3542811aa
%bcond check 0
%global debug_package %{nil}
%global crate memoffset
Name:           rust-memoffset0.5
Version:        0.5.6
Release:        1%{?dist}
Summary:        offset_of functionality for Rust structs.
License:        MIT
URL:            https://crates.io/crates/memoffset
Source0:        https://static.crates.io/crates/memoffset/memoffset-%{version}.crate
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
Summary:        offset_of functionality for Rust structs.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_const-devel
Summary:        offset_of functionality for Rust structs.
BuildArch:      noarch
%description -n %{name}+unstable_const-devel

This package contains library source intended for building other packages which
use the "unstable_const" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_raw-devel
Summary:        offset_of functionality for Rust structs.
BuildArch:      noarch
%description -n %{name}+unstable_raw-devel

This package contains library source intended for building other packages which
use the "unstable_raw" feature of the "%{crate}" crate.

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
%files -n rust-memoffset0.5-devel -f %{oreon_filedir}/rust-memoffset0.5-devel.list

%changelog

%autochangelog
