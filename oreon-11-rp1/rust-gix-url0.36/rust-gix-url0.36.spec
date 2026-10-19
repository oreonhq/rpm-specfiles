%global source0_hash 57d68e70e96da0e5f9c871f1566349e0fd0e1a20bb483c7f54af1dd0b85b4b29
%bcond check 0
%global debug_package %{nil}
%global crate gix-url
Name:           rust-gix-url0.36
Version:        0.36.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project implementing parsing and serializatio...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-url
Source0:        https://static.crates.io/crates/gix-url/gix-url-%{version}.crate
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

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project implementing parsing and serializatio...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project implementing parsing and serializatio...
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
%files -n rust-gix-url0.36-devel -f %{oreon_filedir}/rust-gix-url0.36-devel.list

%changelog

%autochangelog
