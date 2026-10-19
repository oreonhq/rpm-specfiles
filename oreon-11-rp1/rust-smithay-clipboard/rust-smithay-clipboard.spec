%global source0_hash cc8216eec463674a0e90f29e0ae41a4db573ec5b56b1c6c1c71615d249b6d846
%bcond check 0
%global debug_package %{nil}
%global crate smithay-clipboard
Name:           rust-smithay-clipboard
Version:        0.7.2
Release:        1%{?dist}
Summary:        Access to the wayland clipboard for client applications
License:        MIT
URL:            https://crates.io/crates/smithay-clipboard
Source0:        https://static.crates.io/crates/smithay-clipboard/smithay-clipboard-%{version}.crate
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
Summary:        Access to the wayland clipboard for client applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dlopen-devel
Summary:        Access to the wayland clipboard for client applications
BuildArch:      noarch
%description -n %{name}+dlopen-devel

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

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
%files -n rust-smithay-clipboard-devel -f %{oreon_filedir}/rust-smithay-clipboard-devel.list

%changelog

%autochangelog
