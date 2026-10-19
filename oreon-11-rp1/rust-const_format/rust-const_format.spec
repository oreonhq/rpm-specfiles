%global source0_hash 4481a617ad9a412be3b97c5d403fef8ed023103368908b9c50af598ff467cc1e
%bcond check 1
%global debug_package %{nil}
%global crate const_format
Name:           rust-const_format
Version:        0.2.36
Release:        1%{?dist}
Summary:        Compile-time string formatting
License:        Zlib
URL:            https://crates.io/crates/const_format
Source0:        https://static.crates.io/crates/const_format/const_format-%{version}.crate
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
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+assert-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+assert-devel

This package contains library source intended for building other packages which
use the "assert" feature of the "%{crate}" crate.

%package     -n %{name}+assertc-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+assertc-devel

This package contains library source intended for building other packages which
use the "assertc" feature of the "%{crate}" crate.

%package     -n %{name}+assertcp-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+assertcp-devel

This package contains library source intended for building other packages which
use the "assertcp" feature of the "%{crate}" crate.

%package     -n %{name}+const_generics-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+const_generics-devel

This package contains library source intended for building other packages which
use the "const_generics" feature of the "%{crate}" crate.

%package     -n %{name}+constant_time_as_str-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+constant_time_as_str-devel

This package contains library source intended for building other packages which
use the "constant_time_as_str" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+fmt-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+fmt-devel

This package contains library source intended for building other packages which
use the "fmt" feature of the "%{crate}" crate.

%package     -n %{name}+more_str_macros-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+more_str_macros-devel

This package contains library source intended for building other packages which
use the "more_str_macros" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_const_generics-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+nightly_const_generics-devel

This package contains library source intended for building other packages which
use the "nightly_const_generics" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_51-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+rust_1_51-devel

This package contains library source intended for building other packages which
use the "rust_1_51" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_64-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+rust_1_64-devel

This package contains library source intended for building other packages which
use the "rust_1_64" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_83-devel
Summary:        Compile-time string formatting
BuildArch:      noarch
%description -n %{name}+rust_1_83-devel

This package contains library source intended for building other packages which
use the "rust_1_83" feature of the "%{crate}" crate.

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

%cargo_test -f __test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-const_format-devel -f %{oreon_filedir}/rust-const_format-devel.list

%changelog

%autochangelog
