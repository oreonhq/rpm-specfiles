%global source0_hash c5482afe85a0b6ce956c945401598dbc527593c77ba51d0a87a586938b1b893a
%bcond check 0
%global debug_package %{nil}
%global crate spake2
Name:           rust-spake2
Version:        0.4.0
Release:        1%{?dist}
Summary:        SPAKE2 password-authenticated key-exchange algorithm
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/spake2
Source0:        https://static.crates.io/crates/spake2/spake2-%{version}.crate
Patch:          spake2-fix-metadata.diff
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
Summary:        SPAKE2 password-authenticated key-exchange algorithm
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        SPAKE2 password-authenticated key-exchange algorithm
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SPAKE2 password-authenticated key-exchange algorithm
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
%files -n rust-spake2-devel -f %{oreon_filedir}/rust-spake2-devel.list

%changelog

%autochangelog
