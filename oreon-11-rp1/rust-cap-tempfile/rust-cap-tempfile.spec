%global source0_hash 68d8ad5cfac469e58e632590f033d45c66415ef7a8aa801409884818036706f5
%bcond check 0
%global debug_package %{nil}
%global crate cap-tempfile
Name:           rust-cap-tempfile
Version:        3.4.5
Release:        1%{?dist}
Summary:        Capability-based temporary directories
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/cap-tempfile
Source0:        https://static.crates.io/crates/cap-tempfile/cap-tempfile-%{version}.crate
Patch:          cap-tempfile-fix-metadata-auto.diff
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
Summary:        Capability-based temporary directories
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arf_strings-devel
Summary:        Capability-based temporary directories
BuildArch:      noarch
%description -n %{name}+arf_strings-devel

This package contains library source intended for building other packages which
use the "arf_strings" feature of the "%{crate}" crate.

%package     -n %{name}+camino-devel
Summary:        Capability-based temporary directories
BuildArch:      noarch
%description -n %{name}+camino-devel

This package contains library source intended for building other packages which
use the "camino" feature of the "%{crate}" crate.

%package     -n %{name}+fs_utf8-devel
Summary:        Capability-based temporary directories
BuildArch:      noarch
%description -n %{name}+fs_utf8-devel

This package contains library source intended for building other packages which
use the "fs_utf8" feature of the "%{crate}" crate.

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
%files -n rust-cap-tempfile-devel -f %{oreon_filedir}/rust-cap-tempfile-devel.list

%changelog

%autochangelog
