%global source0_hash 082ebe8b7607a68881fbcccc7b3a3e784aa58593ed4261df0679a803fdb80853
%bcond check 1
%global debug_package %{nil}
%global crate anstyle-progress
Name:           rust-anstyle-progress
Version:        0.1.4
Release:        1%{?dist}
Summary:        ANSI escape code progress reporting (OSC 9;4)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-progress
Source0:        https://static.crates.io/crates/anstyle-progress/anstyle-progress-%{version}.crate
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
Summary:        ANSI escape code progress reporting (OSC 9;4)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        ANSI escape code progress reporting (OSC 9;4)
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
%files -n rust-anstyle-progress-devel -f %{oreon_filedir}/rust-anstyle-progress-devel.list

%changelog

%autochangelog
