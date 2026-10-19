%global source0_hash 0b396d1f76d455557e1218ec8066ae14bba60b4b36ecd55577ba979f5db7ecaa
%bcond check 0
%global debug_package %{nil}
%global crate const-default
Name:           rust-const-default
Version:        1.0.0
Release:        1%{?dist}
Summary:        A const Default trait
License:        MIT
URL:            https://crates.io/crates/const-default
Source0:        https://static.crates.io/crates/const-default/const-default-%{version}.crate
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
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+const-default-derive-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+const-default-derive-devel

This package contains library source intended for building other packages which
use the "const-default-derive" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+enable-atomics-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+enable-atomics-devel

This package contains library source intended for building other packages which
use the "enable-atomics" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-docs-devel
Summary:        A const Default trait
BuildArch:      noarch
%description -n %{name}+unstable-docs-devel

This package contains library source intended for building other packages which
use the "unstable-docs" feature of the "%{crate}" crate.

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
%files -n rust-const-default-devel -f %{oreon_filedir}/rust-const-default-devel.list

%changelog

%autochangelog
