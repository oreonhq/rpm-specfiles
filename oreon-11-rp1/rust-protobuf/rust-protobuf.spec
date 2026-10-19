%global source0_hash d65a1d4ddae7d8b5de68153b48f6aa3bba8cb002b243dbdbc55a5afbc98f99f4
%bcond check 0
%global debug_package %{nil}
%global crate protobuf
Name:           rust-protobuf
Version:        3.7.2
Release:        1%{?dist}
Summary:        Rust implementation of Google protocol buffers
License:        MIT
URL:            https://crates.io/crates/protobuf
Source0:        https://static.crates.io/crates/protobuf/protobuf-%{version}.crate
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
Summary:        Rust implementation of Google protocol buffers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Rust implementation of Google protocol buffers
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+with-bytes-devel
Summary:        Rust implementation of Google protocol buffers
BuildArch:      noarch
%description -n %{name}+with-bytes-devel

This package contains library source intended for building other packages which
use the "with-bytes" feature of the "%{crate}" crate.

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
%files -n rust-protobuf-devel -f %{oreon_filedir}/rust-protobuf-devel.list

%changelog

%autochangelog
