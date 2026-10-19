%global source0_hash 4ab587f5395da16dd2e6939adf53dede583221b320cadfb94e02b5b7b9bf24cc
%bcond check 0
%global debug_package %{nil}
%global crate ansiterm
Name:           rust-ansiterm
Version:        0.12.2
Release:        1%{?dist}
Summary:        Library for ANSI terminal colours and styles (bold, underline)
License:        MIT
URL:            https://crates.io/crates/ansiterm
Source0:        https://static.crates.io/crates/ansiterm/ansiterm-%{version}.crate
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

%package     -n %{name}+ansi_colours-devel
Summary:        Library for ANSI terminal colours and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+ansi_colours-devel

This package contains library source intended for building other packages which
use the "ansi_colours" feature of the "%{crate}" crate.

%package     -n %{name}+derive_serde_style-devel
Summary:        Library for ANSI terminal colours and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+derive_serde_style-devel

This package contains library source intended for building other packages which
use the "derive_serde_style" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for ANSI terminal colours and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-ansiterm-devel -f %{oreon_filedir}/rust-ansiterm-devel.list

%changelog

%autochangelog
