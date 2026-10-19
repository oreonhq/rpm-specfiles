%global source0_hash 01200283c7e9307b1afee820eea16008048b6712ef768617e18f36aadb1ed272
%bcond check 1
%global debug_package %{nil}
%global crate jid
Name:           rust-jid
Version:        0.12.3
Release:        1%{?dist}
Summary:        Jid struct for Jabber IDs
License:        MPL-2.0
URL:            https://crates.io/crates/jid
Source0:        https://static.crates.io/crates/jid/jid-%{version}.crate
Patch:          jid-fix-metadata.diff
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
Summary:        Jid struct for Jabber IDs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+quote-devel
Summary:        Jid struct for Jabber IDs
BuildArch:      noarch
%description -n %{name}+quote-devel

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Jid struct for Jabber IDs
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-jid-devel -f %{oreon_filedir}/rust-jid-devel.list

%changelog

%autochangelog
