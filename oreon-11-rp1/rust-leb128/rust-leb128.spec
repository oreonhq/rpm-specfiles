%global source0_hash 884e2677b40cc8c339eaefcb701c32ef1fd2493d71118dc0ca4b6a736c93bd67
%bcond check 0
%global crate leb128
Name:           rust-leb128
Version:        0.2.5
Release:        1%{?dist}
Summary:        DWARF's LEB128 encoding library and REPL
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/leb128
Source0:        https://static.crates.io/crates/leb128/leb128-%{version}.crate
Patch:          leb128-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        DWARF's LEB128 encoding library and REPL
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        DWARF's LEB128 encoding library and REPL
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        DWARF's LEB128 encoding library and REPL
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n leb128 -f %{oreon_filedir}/leb128.list
%files -n rust-leb128-devel -f %{oreon_filedir}/rust-leb128-devel.list

%changelog

%autochangelog
