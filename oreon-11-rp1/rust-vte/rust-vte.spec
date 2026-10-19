%global source0_hash a5924018406ce0063cd67f8e008104968b74b563ee1b85dde3ed1f7cb87d3dbd
%bcond check 0
%global debug_package %{nil}
%global crate vte
Name:           rust-vte
Version:        0.15.0
Release:        1%{?dist}
Summary:        Parser for implementing terminal emulators
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/vte
Source0:        https://static.crates.io/crates/vte/vte-%{version}.crate
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
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+ansi-devel

This package contains library source intended for building other packages which
use the "ansi" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Parser for implementing terminal emulators
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
%files -n rust-vte-devel -f %{oreon_filedir}/rust-vte-devel.list

%changelog

%autochangelog
