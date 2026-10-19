%global source0_hash d1fcb8ef5b16bcf874abe9b68d8abb3c0493c876d367ab824151f30a0f3f3756
%bcond check 0
%global debug_package %{nil}
%global crate gix-glob
Name:           rust-gix-glob0.26
Version:        0.26.1
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dealing with pattern matching
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-glob
Source0:        https://static.crates.io/crates/gix-glob/gix-glob-%{version}.crate
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
Summary:        A crate of the gitoxide project dealing with pattern matching
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project dealing with pattern matching
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
%files -n rust-gix-glob0.26-devel -f %{oreon_filedir}/rust-gix-glob0.26-devel.list

%changelog

%autochangelog
