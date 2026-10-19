%global source0_hash 5ab627f34ff61b80d756180d556f9c68801d836d271b3b8c094504ceca69d221
%bcond check 0
%global debug_package %{nil}
%global crate xml5ever
Name:           rust-xml5ever0.39
Version:        0.39.0
Release:        1%{?dist}
Summary:        Push based streaming parser for XML
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/xml5ever
Source0:        https://static.crates.io/crates/xml5ever/xml5ever-%{version}.crate
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
Summary:        Push based streaming parser for XML
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Push based streaming parser for XML
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+trace_tokenizer-devel
Summary:        Push based streaming parser for XML
BuildArch:      noarch
%description -n %{name}+trace_tokenizer-devel

This package contains library source intended for building other packages which
use the "trace_tokenizer" feature of the "%{crate}" crate.

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
%files -n rust-xml5ever0.39-devel -f %{oreon_filedir}/rust-xml5ever0.39-devel.list

%changelog

%autochangelog
