%global source0_hash 639504390a22f3fa372b16088d0569448274ef04379ff798437aab3cf811093e
%bcond check 0
%global debug_package %{nil}
%global crate completest-pty
Name:           rust-completest-pty
Version:        1.1.0
Release:        1%{?dist}
Summary:        Run completions for your program
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/completest-pty
Source0:        https://static.crates.io/crates/completest-pty/completest-pty-%{version}.crate
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
Summary:        Run completions for your program
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
%files -n rust-completest-pty-devel -f %{oreon_filedir}/rust-completest-pty-devel.list

%changelog

%autochangelog
