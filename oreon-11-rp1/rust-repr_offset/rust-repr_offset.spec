%global source0_hash fb1070755bd29dffc19d0971cab794e607839ba2ef4b69a9e6fbc8733c1b72ea
%bcond check 0
%global debug_package %{nil}
%global crate repr_offset
Name:           rust-repr_offset
Version:        0.2.2
Release:        1%{?dist}
Summary:        Offsets of fields for types with a stable layout.
License:        Zlib
URL:            https://crates.io/crates/repr_offset
Source0:        https://static.crates.io/crates/repr_offset/repr_offset-%{version}.crate
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
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+for_examples-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+for_examples-devel

This package contains library source intended for building other packages which
use the "for_examples" feature of the "%{crate}" crate.

%package     -n %{name}+priv_expensive_test-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+priv_expensive_test-devel

This package contains library source intended for building other packages which
use the "priv_expensive_test" feature of the "%{crate}" crate.

%package     -n %{name}+priv_raw_ref-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+priv_raw_ref-devel

This package contains library source intended for building other packages which
use the "priv_raw_ref" feature of the "%{crate}" crate.

%package     -n %{name}+repr_offset_derive-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+repr_offset_derive-devel

This package contains library source intended for building other packages which
use the "repr_offset_derive" feature of the "%{crate}" crate.

%package     -n %{name}+test_nightly-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+test_nightly-devel

This package contains library source intended for building other packages which
use the "test_nightly" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Offsets of fields for types with a stable layout.
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

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
%files -n rust-repr_offset-devel -f %{oreon_filedir}/rust-repr_offset-devel.list

%changelog

%autochangelog
