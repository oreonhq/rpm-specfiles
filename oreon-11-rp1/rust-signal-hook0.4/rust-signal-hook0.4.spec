%global source0_hash b2a0c28ca5908dbdbcd52e6fdaa00358ab88637f8ab33e1f188dd510eb44b53d
%bcond check 0
%global debug_package %{nil}
%global crate signal-hook
Name:           rust-signal-hook0.4
Version:        0.4.4
Release:        1%{?dist}
Summary:        Unix signal handling
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/signal-hook
Source0:        https://static.crates.io/crates/signal-hook/signal-hook-%{version}.crate
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
Summary:        Unix signal handling
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+channel-devel
Summary:        Unix signal handling
BuildArch:      noarch
%description -n %{name}+channel-devel

This package contains library source intended for building other packages which
use the "channel" feature of the "%{crate}" crate.

%package     -n %{name}+extended-siginfo-devel
Summary:        Unix signal handling
BuildArch:      noarch
%description -n %{name}+extended-siginfo-devel

This package contains library source intended for building other packages which
use the "extended-siginfo" feature of the "%{crate}" crate.

%package     -n %{name}+extended-siginfo-raw-devel
Summary:        Unix signal handling
BuildArch:      noarch
%description -n %{name}+extended-siginfo-raw-devel

This package contains library source intended for building other packages which
use the "extended-siginfo-raw" feature of the "%{crate}" crate.

%package     -n %{name}+iterator-devel
Summary:        Unix signal handling
BuildArch:      noarch
%description -n %{name}+iterator-devel

This package contains library source intended for building other packages which
use the "iterator" feature of the "%{crate}" crate.

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
%files -n rust-signal-hook0.4-devel -f %{oreon_filedir}/rust-signal-hook0.4-devel.list

%changelog

%autochangelog
