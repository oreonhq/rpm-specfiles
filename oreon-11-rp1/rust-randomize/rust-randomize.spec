%global source0_hash 88c38c99b51f33c9fcc655252bf02ac8048eb70f35244e4697b0de9c473e940a
%bcond check 1
%global debug_package %{nil}
%global crate randomize
Name:           rust-randomize
Version:        3.0.1
Release:        1%{?dist}
Summary:        randomization routines
License:        0BSD
URL:            https://crates.io/crates/randomize
Source0:        https://static.crates.io/crates/randomize/randomize-%{version}.crate
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
Summary:        randomization routines
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
rm -f %{buildroot}%{_bindir}/randomize
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-randomize-devel -f %{oreon_filedir}/rust-randomize-devel.list

%changelog

%autochangelog
