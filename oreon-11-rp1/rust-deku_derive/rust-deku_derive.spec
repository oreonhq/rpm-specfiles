%global source0_hash bec2a42b511fc5efd9183f4f71c17885d627b17e7fd9a61a92089406caa4397e
%bcond check 0
%global debug_package %{nil}
%global crate deku_derive
Name:           rust-deku_derive
Version:        0.20.3
Release:        1%{?dist}
Summary:        Bit level serialization/deserialization proc-macro for structs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/deku_derive
Source0:        https://static.crates.io/crates/deku_derive/deku_derive-%{version}.crate
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
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bits-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+bits-devel

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+no-assert-string-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+no-assert-string-devel

This package contains library source intended for building other packages which
use the "no-assert-string" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-crate-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+proc-macro-crate-devel

This package contains library source intended for building other packages which
use the "proc-macro-crate" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-deku_derive-devel -f %{oreon_filedir}/rust-deku_derive-devel.list

%changelog

%autochangelog
