%global source0_hash 4dae8780f63ed8a803b8bdabbd7aa5f5c5d74592c8b50eed875c1bb4f6545a6a
%bcond check 0
%global debug_package %{nil}
%global crate gix-validate
Name:           rust-gix-validate0.11
Version:        0.11.4
Release:        1%{?dist}
Summary:        Validation functions for various kinds of names in git
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-validate
Source0:        https://static.crates.io/crates/gix-validate/gix-validate-%{version}.crate
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
Summary:        Validation functions for various kinds of names in git
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
%files -n rust-gix-validate0.11-devel -f %{oreon_filedir}/rust-gix-validate0.11-devel.list

%changelog

%autochangelog
