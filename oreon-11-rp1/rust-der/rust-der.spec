%global source0_hash a878c850e9e421b20262e9b41f9c860e4785fa07541c266b62ff9d1ef998a80a
%bcond check 0
%global debug_package %{nil}
%global crate der
Name:           rust-der
Version:        0.8.2
Release:        1%{?dist}
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/der
Source0:        https://static.crates.io/crates/der/der-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+flagset-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+flagset-devel

This package contains library source intended for building other packages which
use the "flagset" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+real-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+real-devel

This package contains library source intended for building other packages which
use the "real" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encod...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-der-devel -f %{oreon_filedir}/rust-der-devel.list

%changelog

%autochangelog
