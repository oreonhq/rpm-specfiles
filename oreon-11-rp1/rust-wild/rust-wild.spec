%global source0_hash a3131afc8c575281e1e80f36ed6a092aa502c08b18ed7524e86fbbb12bb410e1
%bcond check 0
%global debug_package %{nil}
%global crate wild
Name:           rust-wild
Version:        2.2.1
Release:        1%{?dist}
Summary:        Glob (wildcard) expanded command-line arguments
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/wild
Source0:        https://static.crates.io/crates/wild/wild-%{version}.crate
Patch:          wild-fix-metadata-auto.diff
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
Summary:        Glob (wildcard) expanded command-line arguments
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+glob-quoted-on-windows-devel
Summary:        Glob (wildcard) expanded command-line arguments
BuildArch:      noarch
%description -n %{name}+glob-quoted-on-windows-devel

This package contains library source intended for building other packages which
use the "glob-quoted-on-windows" feature of the "%{crate}" crate.

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
%files -n rust-wild-devel -f %{oreon_filedir}/rust-wild-devel.list

%changelog

%autochangelog
