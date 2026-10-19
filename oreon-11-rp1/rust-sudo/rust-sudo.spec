%global source0_hash 88bd84d4c082e18e37fef52c0088e4407dabcef19d23a607fb4b5ee03b7d5b83
%bcond check 0
%global debug_package %{nil}
%global crate sudo
Name:           rust-sudo
Version:        0.6.0
Release:        1%{?dist}
Summary:        Detect if you are running as root, restart self with sudo if needed or setup uid zero when running with the SUID flag set
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sudo
Source0:        https://static.crates.io/crates/sudo/sudo-%{version}.crate
Patch:          sudo-fix-metadata.diff
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
Summary:        Detect if you are running as root, restart self with sudo if needed or setup uid zero when running with the SUID flag set
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
%files -n rust-sudo-devel -f %{oreon_filedir}/rust-sudo-devel.list

%changelog

%autochangelog
