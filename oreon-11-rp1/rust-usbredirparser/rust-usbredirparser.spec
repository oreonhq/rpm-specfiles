%global source0_hash e2aa71a0a0678a421d34b5127a3b3a042d6303a37f25b3844569779115df74f8
%bcond check 1
%global debug_package %{nil}
%global crate usbredirparser
Name:           rust-usbredirparser
Version:        0.4.1
Release:        1%{?dist}
Summary:        Bindings for usbredirparser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/usbredirparser
Source0:        https://static.crates.io/crates/usbredirparser/usbredirparser-%{version}.crate
ExcludeArch:    i686
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
Summary:        Bindings for usbredirparser
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
%files -n rust-usbredirparser-devel -f %{oreon_filedir}/rust-usbredirparser-devel.list

%changelog

%autochangelog
