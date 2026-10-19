%global source0_hash 71f4fe417e8cc3bb9b437dfa9290ce92bd2730ba5374719bdfd9147fbc8f17cd
%bcond check 1
%global debug_package %{nil}
%global crate base2048
Name:           rust-base2048
Version:        2.0.2
Release:        1%{?dist}
Summary:        Encoding for efficient encoding of binary data on twitter
License:        0BSD
URL:            https://crates.io/crates/base2048
Source0:        https://static.crates.io/crates/base2048/base2048-%{version}.crate
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
Summary:        Encoding for efficient encoding of binary data on twitter
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
chmod -x src/lib.rs
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
%files -n rust-base2048-devel -f %{oreon_filedir}/rust-base2048-devel.list

%changelog

%autochangelog
