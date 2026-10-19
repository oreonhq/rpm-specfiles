%global source0_hash 89e515aa4699a88148ed5ef96413ceef0048ce95b43fbc955a33bde0a70fcae6
%bcond check 0
%global debug_package %{nil}
%global crate shellwords
Name:           rust-shellwords
Version:        1.1.0
Release:        1%{?dist}
Summary:        Manipulate strings according to the word parsing rules of the UNIX Bourne shell
License:        MIT
URL:            https://crates.io/crates/shellwords
Source0:        https://static.crates.io/crates/shellwords/shellwords-%{version}.crate
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
Summary:        Manipulate strings according to the word parsing rules of the UNIX Bourne shell
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
%files -n rust-shellwords-devel -f %{oreon_filedir}/rust-shellwords-devel.list

%changelog

%autochangelog
