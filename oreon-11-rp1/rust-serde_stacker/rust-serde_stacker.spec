%global source0_hash d4936375d50c4be7eff22293a9344f8e46f323ed2b3c243e52f89138d9bb0f4a
%bcond check 1
%global debug_package %{nil}
%global crate serde_stacker
Name:           rust-serde_stacker
Version:        0.1.14
Release:        1%{?dist}
Summary:        Serde adapter that avoids stack overflow by dynamically growing the stack
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_stacker
Source0:        https://static.crates.io/crates/serde_stacker/serde_stacker-%{version}.crate
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
Summary:        Serde adapter that avoids stack overflow by dynamically growing the stack
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
%files -n rust-serde_stacker-devel -f %{oreon_filedir}/rust-serde_stacker-devel.list

%changelog

%autochangelog
