%global source0_hash e8df223a361486eb5834f99b3c81de685342ea9f6c7eba8c40a7e4a136f64243
%bcond check 0
%global debug_package %{nil}
%global crate nu-engine
Name:           rust-nu-engine
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell's evaluation engine
License:        MIT
URL:            https://crates.io/crates/nu-engine
Source0:        https://static.crates.io/crates/nu-engine/nu-engine-%{version}.crate
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
Summary:        Nushell's evaluation engine
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+plugin-devel
Summary:        Nushell's evaluation engine
BuildArch:      noarch
%description -n %{name}+plugin-devel

This package contains library source intended for building other packages which
use the "plugin" feature of the "%{crate}" crate.

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
%files -n rust-nu-engine-devel -f %{oreon_filedir}/rust-nu-engine-devel.list

%changelog

%autochangelog
