%global source0_hash d2ee4885492bb655bfa05d039cd9163eb8fe9f79ddebf00ca23a1637510c2fd2
%bcond check 1
%global debug_package %{nil}
%global crate scientific-macro
Name:           rust-scientific-macro
Version:        0.5.2
Release:        1%{?dist}
Summary:        Macro for scientific, the arbitrary precision scientific number
License:        MIT
URL:            https://crates.io/crates/scientific-macro
Source0:        https://static.crates.io/crates/scientific-macro/scientific-macro-%{version}.crate
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
Summary:        Macro for scientific, the arbitrary precision scientific number
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-scientific-macro-devel -f %{oreon_filedir}/rust-scientific-macro-devel.list

%changelog

%autochangelog
