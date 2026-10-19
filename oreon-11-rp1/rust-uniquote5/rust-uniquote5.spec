%global source0_hash b56132e1afba089ff971694f5fa858b1b715b58156bd1f1503d6d0a6c3c779f8
%bcond check 0
%global debug_package %{nil}
%global crate uniquote
Name:           rust-uniquote5
Version:        5.0.0
Release:        1%{?dist}
Summary:        Quote strings for clear display in output
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://crates.io/crates/uniquote
Source0:        https://static.crates.io/crates/uniquote/uniquote-%{version}.crate
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
Summary:        Quote strings for clear display in output
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Quote strings for clear display in output
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+os_str_bytes-devel
Summary:        Quote strings for clear display in output
BuildArch:      noarch
%description -n %{name}+os_str_bytes-devel

This package contains library source intended for building other packages which
use the "os_str_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Quote strings for clear display in output
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
%files -n rust-uniquote5-devel -f %{oreon_filedir}/rust-uniquote5-devel.list

%changelog

%autochangelog
