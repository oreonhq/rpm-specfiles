%global source0_hash 5fed54709c5b3a53d09bb1c113ea4f5ceafd1e772ddcb0030a82e1d56c087b08
%bcond check 0
%global debug_package %{nil}
%global crate tendril
Name:           rust-tendril0.5
Version:        0.5.1
Release:        1%{?dist}
Summary:        Compact buffer/string type for zero-copy parsing
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tendril
Source0:        https://static.crates.io/crates/tendril/tendril-%{version}.crate
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
Summary:        Compact buffer/string type for zero-copy parsing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+encoding_rs-devel
Summary:        Compact buffer/string type for zero-copy parsing
BuildArch:      noarch
%description -n %{name}+encoding_rs-devel

This package contains library source intended for building other packages which
use the "encoding_rs" feature of the "%{crate}" crate.

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
%files -n rust-tendril0.5-devel -f %{oreon_filedir}/rust-tendril0.5-devel.list

%changelog

%autochangelog
