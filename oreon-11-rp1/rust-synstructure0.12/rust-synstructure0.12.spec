%global source0_hash f36bdaa60a83aca3921b5259d5400cbf5e90fc51931376a9bd4a0eb79aa7210f
%bcond check 1
%global debug_package %{nil}
%global crate synstructure
Name:           rust-synstructure0.12
Version:        0.12.6
Release:        1%{?dist}
Summary:        Helper methods and macros for custom derives
License:        MIT
URL:            https://crates.io/crates/synstructure
Source0:        https://static.crates.io/crates/synstructure/synstructure-%{version}.crate
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
Summary:        Helper methods and macros for custom derives
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-devel
Summary:        Helper methods and macros for custom derives
BuildArch:      noarch
%description -n %{name}+proc-macro-devel

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i 's/&mut FnMut/\&mut dyn FnMut/g' src/lib.rs
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
%files -n rust-synstructure0.12-devel -f %{oreon_filedir}/rust-synstructure0.12-devel.list

%changelog

%autochangelog
