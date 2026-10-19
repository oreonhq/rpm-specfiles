%global source0_hash ebf55291257a2a5c90cf50ae17b6bbaabc3fd13642cf3895a71c412513c19630
%bcond check 0
%global debug_package %{nil}
%global crate deku
Name:           rust-deku
Version:        0.20.3
Release:        1%{?dist}
Summary:        Bit level serialization/deserialization proc-macro for structs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/deku
Source0:        https://static.crates.io/crates/deku/deku-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+bits-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+bits-devel

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

%package     -n %{name}+error_in_core-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+error_in_core-devel

This package contains library source intended for building other packages which
use the "error_in_core" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Bit level serialization/deserialization proc-macro for structs
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

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
%files -n rust-deku-devel -f %{oreon_filedir}/rust-deku-devel.list

%changelog

%autochangelog
