%global source0_hash f3a53fac24f34a81bc9954b5d6cfce0c21e18ec6959f44f56e8e90e4bb7c346c
%bcond check 0
%global debug_package %{nil}
%global crate bzip2
Name:           rust-bzip2_0.6
Version:        0.6.1
Release:        1%{?dist}
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bzip2
Source0:        https://static.crates.io/crates/bzip2/bzip2-%{version}.crate
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
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bzip2-sys-devel
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams
BuildArch:      noarch
%description -n %{name}+bzip2-sys-devel

This package contains library source intended for building other packages which
use the "bzip2-sys" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

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
%files -n rust-bzip2_0.6-devel -f %{oreon_filedir}/rust-bzip2_0.6-devel.list

%changelog

%autochangelog
