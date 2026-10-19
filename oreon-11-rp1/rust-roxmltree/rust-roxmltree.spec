%global source0_hash f1964b10c76125c36f8afe190065a4bf9a87bf324842c05701330bba9f1cacbb
%bcond check 1
%global debug_package %{nil}
%global crate roxmltree
Name:           rust-roxmltree
Version:        0.21.1
Release:        1%{?dist}
Summary:        Represent an XML as a read-only tree
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/roxmltree
Source0:        https://static.crates.io/crates/roxmltree/roxmltree-%{version}.crate
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
Summary:        Represent an XML as a read-only tree
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+positions-devel
Summary:        Represent an XML as a read-only tree
BuildArch:      noarch
%description -n %{name}+positions-devel

This package contains library source intended for building other packages which
use the "positions" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Represent an XML as a read-only tree
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
%files -n rust-roxmltree-devel -f %{oreon_filedir}/rust-roxmltree-devel.list

%changelog

%autochangelog
