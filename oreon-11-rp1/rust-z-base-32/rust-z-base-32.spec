%global source0_hash 44f94003b56f8f812c88dd188d9bafc71d8e3786fd04812c2d8cdb176810ceb4
%bcond check 0
%global debug_package %{nil}
%global crate z-base-32
Name:           rust-z-base-32
Version:        0.1.5
Release:        1%{?dist}
Summary:        z-base-32: human-oriented base-32 encoding
License:        MIT
URL:            https://crates.io/crates/z-base-32
Source0:        https://static.crates.io/crates/z-base-32/z-base-32-%{version}.crate
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

%package     -n %{name}+cli-devel
Summary:        z-base-32: human-oriented base-32 encoding
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+python-devel
Summary:        z-base-32: human-oriented base-32 encoding
BuildArch:      noarch
%description -n %{name}+python-devel

This package contains library source intended for building other packages which
use the "python" feature of the "%{crate}" crate.

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
%files -n rust-z-base-32-devel -f %{oreon_filedir}/rust-z-base-32-devel.list

%changelog

%autochangelog
