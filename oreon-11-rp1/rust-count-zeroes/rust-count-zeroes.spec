%global source0_hash a233b11d956f785d539dd960035744d041d75c272d7c6e95285bbcc8b4a7c172
%bcond check 0
%global crate count-zeroes
Name:           rust-count-zeroes
Version:        0.2.1
Release:        1%{?dist}
Summary:        Count zeroes on a disk or a file
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/count-zeroes
Source0:        https://static.crates.io/crates/count-zeroes/count-zeroes-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Count zeroes on a disk or a file
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Count zeroes on a disk or a file
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n count-zeroes -f %{oreon_filedir}/count-zeroes.list
%files -n rust-count-zeroes-devel -f %{oreon_filedir}/rust-count-zeroes-devel.list

%changelog

%autochangelog
