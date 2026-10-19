%global source0_hash 9a65843dfefbafd3c879c683306959a6de478443ffe9c9adf02f5976432402d7
%bcond check 0
%global debug_package %{nil}
%global crate pretty-hex
Name:           rust-pretty-hex
Version:        0.4.2
Release:        1%{?dist}
Summary:        Pretty hex dump of bytes slice in the common style
License:        MIT
URL:            https://crates.io/crates/pretty-hex
Source0:        https://static.crates.io/crates/pretty-hex/pretty-hex-%{version}.crate
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
Summary:        Pretty hex dump of bytes slice in the common style
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pretty hex dump of bytes slice in the common style
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

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
%files -n rust-pretty-hex-devel -f %{oreon_filedir}/rust-pretty-hex-devel.list

%changelog

%autochangelog
