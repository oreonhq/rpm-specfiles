%global source0_hash f9395f0f0eee849a9b707b2f06bb92a6a422090e2123bb2ef8e87a0e61892a8e
%bcond check 1
%global debug_package %{nil}
%global crate smallvec
Name:           rust-smallvec
Version:        1.16.2
Release:        1%{?dist}
Summary:        'Small vector' optimization: store up to a small number of items on
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/smallvec
Source0:        https://static.crates.io/crates/smallvec/smallvec-%{version}.crate
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
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+const_generics-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+const_generics-devel

This package contains library source intended for building other packages which
use the "const_generics" feature of the "%{crate}" crate.

%package     -n %{name}+const_new-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+const_new-devel

This package contains library source intended for building other packages which
use the "const_new" feature of the "%{crate}" crate.

%package     -n %{name}+drain_filter-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+drain_filter-devel

This package contains library source intended for building other packages which
use the "drain_filter" feature of the "%{crate}" crate.

%package     -n %{name}+drain_keep_rest-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+drain_keep_rest-devel

This package contains library source intended for building other packages which
use the "drain_keep_rest" feature of the "%{crate}" crate.

%package     -n %{name}+impl_bincode-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+impl_bincode-devel

This package contains library source intended for building other packages which
use the "impl_bincode" feature of the "%{crate}" crate.

%package     -n %{name}+may_dangle-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+may_dangle-devel

This package contains library source intended for building other packages which
use the "may_dangle" feature of the "%{crate}" crate.

%package     -n %{name}+specialization-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+specialization-devel

This package contains library source intended for building other packages which
use the "specialization" feature of the "%{crate}" crate.

%package     -n %{name}+union-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+union-devel

This package contains library source intended for building other packages which
use the "union" feature of the "%{crate}" crate.

%package     -n %{name}+write-devel
Summary:        'Small vector' optimization: store up to a small number of items on
BuildArch:      noarch
%description -n %{name}+write-devel

This package contains library source intended for building other packages which
use the "write" feature of the "%{crate}" crate.

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
%files -n rust-smallvec-devel -f %{oreon_filedir}/rust-smallvec-devel.list

%changelog

%autochangelog
