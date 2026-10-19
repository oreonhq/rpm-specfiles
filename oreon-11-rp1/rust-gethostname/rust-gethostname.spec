%global source0_hash 1bd49230192a3797a9a4d6abe9b3eed6f7fa4c8a8a4947977c6f80025f92cbd8
%bcond check 0
%global debug_package %{nil}
%global crate gethostname
Name:           rust-gethostname
Version:        1.1.0
Release:        1%{?dist}
Summary:        gethostname for all platforms
License:        Apache-2.0
URL:            https://crates.io/crates/gethostname
Source0:        https://static.crates.io/crates/gethostname/gethostname-%{version}.crate
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
Summary:        gethostname for all platforms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-gethostname-devel -f %{oreon_filedir}/rust-gethostname-devel.list

%changelog

%autochangelog
