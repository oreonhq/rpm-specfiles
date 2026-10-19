%global source0_hash d4219a5aadc4844073d134e27fd52228933a462fbd07fe51ac5df8393f08168a
%bcond check 1
%global debug_package %{nil}
%global crate zlink-macros
Name:           rust-zlink-macros
Version:        0.4.0
Release:        1%{?dist}
Summary:        Macros providing the high-level zlink API
License:        MIT
URL:            https://crates.io/crates/zlink-macros
Source0:        https://static.crates.io/crates/zlink-macros/zlink-macros-%{version}.crate
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
Summary:        Macros providing the high-level zlink API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+idl-parse-devel
Summary:        Macros providing the high-level zlink API
BuildArch:      noarch
%description -n %{name}+idl-parse-devel

This package contains library source intended for building other packages which
use the "idl-parse" feature of the "%{crate}" crate.

%package     -n %{name}+introspection-devel
Summary:        Macros providing the high-level zlink API
BuildArch:      noarch
%description -n %{name}+introspection-devel

This package contains library source intended for building other packages which
use the "introspection" feature of the "%{crate}" crate.

%package     -n %{name}+proxy-devel
Summary:        Macros providing the high-level zlink API
BuildArch:      noarch
%description -n %{name}+proxy-devel

This package contains library source intended for building other packages which
use the "proxy" feature of the "%{crate}" crate.

%package     -n %{name}+service-devel
Summary:        Macros providing the high-level zlink API
BuildArch:      noarch
%description -n %{name}+service-devel

This package contains library source intended for building other packages which
use the "service" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Macros providing the high-level zlink API
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%cargo_test -- --test doc_comments
%cargo_test -- --test enum_errors
%cargo_test -- --test introspect-custom-type
%cargo_test -- --test introspect-reply-error
%cargo_test -- --test introspect-type
%cargo_test -- --test lifetime_removal
%cargo_test -- --test reply-error-derive
%cargo_test -- --test reply-error-empty
%cargo_test -- --test reply-error-simple
%cargo_test -- --test tuple_variant_errors
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-zlink-macros-devel -f %{oreon_filedir}/rust-zlink-macros-devel.list

%changelog

%autochangelog
