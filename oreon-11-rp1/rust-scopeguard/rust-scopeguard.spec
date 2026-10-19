%global source0_hash 94143f37725109f92c262ed2cf5e59bce7498c01bcc1502d7b9afe439a4e9f49
%bcond_without check
%global debug_package %{nil}
%global crate scopeguard
Name:           rust-scopeguard
Version:        1.2.0
Release:        1%{?dist}
Summary:        RAII scope guard that will run a given closure when it goes out of scope
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/scopeguard
Source0:        https://static.crates.io/crates/scopeguard/scopeguard-%{version}.crate
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
Summary:        RAII scope guard that will run a given closure when it goes out of scope
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        RAII scope guard that will run a given closure when it goes out of scope
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
%files -n rust-scopeguard-devel -f %{oreon_filedir}/rust-scopeguard-devel.list

%changelog

%autochangelog
