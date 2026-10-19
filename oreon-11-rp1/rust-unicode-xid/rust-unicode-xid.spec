%global source0_hash ebc1c04c71510c7f702b52b7c350734c9ff1295c464a03335b00bb84fc54f853
%bcond check 0
%global debug_package %{nil}
%global crate unicode-xid
Name:           rust-unicode-xid
Version:        0.2.6
Release:        1%{?dist}
Summary:        Determine whether characters have the XID_Start
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-xid
Source0:        https://static.crates.io/crates/unicode-xid/unicode-xid-%{version}.crate
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
Summary:        Determine whether characters have the XID_Start
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        Determine whether characters have the XID_Start
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Determine whether characters have the XID_Start
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

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
%files -n rust-unicode-xid-devel -f %{oreon_filedir}/rust-unicode-xid-devel.list

%changelog

%autochangelog
