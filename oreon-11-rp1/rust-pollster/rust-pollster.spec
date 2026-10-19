%global source0_hash 22686f4785f02a4fcc856d3b3bb19bf6c8160d103f7a99cc258bddd0251dc7f2
%bcond check 0
%global debug_package %{nil}
%global crate pollster
Name:           rust-pollster
Version:        0.3.0
Release:        1%{?dist}
Summary:        Synchronously block the thread until a future completes
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pollster
Source0:        https://static.crates.io/crates/pollster/pollster-%{version}.crate
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
Summary:        Synchronously block the thread until a future completes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+macro-devel
Summary:        Synchronously block the thread until a future completes
BuildArch:      noarch
%description -n %{name}+macro-devel

This package contains library source intended for building other packages which
use the "macro" feature of the "%{crate}" crate.

%package     -n %{name}+pollster-macro-devel
Summary:        Synchronously block the thread until a future completes
BuildArch:      noarch
%description -n %{name}+pollster-macro-devel

This package contains library source intended for building other packages which
use the "pollster-macro" feature of the "%{crate}" crate.

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
%files -n rust-pollster-devel -f %{oreon_filedir}/rust-pollster-devel.list

%changelog

%autochangelog
