%global source0_hash d6790f58c7ff633d8771f42965289203411a5e5c68388703c06e14f24770b41e
%bcond check 1
%global debug_package %{nil}
%global crate oorandom
Name:           rust-oorandom
Version:        11.1.5
Release:        1%{?dist}
Summary:        A tiny, robust PRNG implementation
License:        MIT
URL:            https://crates.io/crates/oorandom
Source0:        https://static.crates.io/crates/oorandom/oorandom-%{version}.crate
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
Summary:        A tiny, robust PRNG implementation
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
%files -n rust-oorandom-devel -f %{oreon_filedir}/rust-oorandom-devel.list

%changelog

%autochangelog
