%global source0_hash fce91f2f0ec87dff7e6bcbbeb267439aa1188703003c6055193c821487400432
%bcond check 1
%global debug_package %{nil}
%global crate tabwriter
Name:           rust-tabwriter
Version:        1.4.1
Release:        1%{?dist}
Summary:        Elastic tabstops
License:        Unlicense OR MIT
URL:            https://crates.io/crates/tabwriter
Source0:        https://static.crates.io/crates/tabwriter/tabwriter-%{version}.crate
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
Summary:        Elastic tabstops
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi_formatting-devel
Summary:        Elastic tabstops
BuildArch:      noarch
%description -n %{name}+ansi_formatting-devel

This package contains library source intended for building other packages which
use the "ansi_formatting" feature of the "%{crate}" crate.

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
%files -n rust-tabwriter-devel -f %{oreon_filedir}/rust-tabwriter-devel.list

%changelog

%autochangelog
