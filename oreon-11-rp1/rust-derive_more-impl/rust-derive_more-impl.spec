%global source0_hash 799a97264921d8623a957f6c3b9011f3b5492f557bbb7a5a19b7fa6d06ba8dcb
%bcond check 1
%global debug_package %{nil}
%global crate derive_more-impl
Name:           rust-derive_more-impl
Version:        2.1.1
Release:        1%{?dist}
Summary:        Internal implementation of derive_more crate
License:        MIT
URL:            https://crates.io/crates/derive_more-impl
Source0:        https://static.crates.io/crates/derive_more-impl/derive_more-impl-%{version}.crate
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
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+add-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+add-devel

This package contains library source intended for building other packages which
use the "add" feature of the "%{crate}" crate.

%package     -n %{name}+add_assign-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+add_assign-devel

This package contains library source intended for building other packages which
use the "add_assign" feature of the "%{crate}" crate.

%package     -n %{name}+as_ref-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+as_ref-devel

This package contains library source intended for building other packages which
use the "as_ref" feature of the "%{crate}" crate.

%package     -n %{name}+constructor-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+constructor-devel

This package contains library source intended for building other packages which
use the "constructor" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+deref-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+deref-devel

This package contains library source intended for building other packages which
use the "deref" feature of the "%{crate}" crate.

%package     -n %{name}+deref_mut-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+deref_mut-devel

This package contains library source intended for building other packages which
use the "deref_mut" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+eq-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+eq-devel

This package contains library source intended for building other packages which
use the "eq" feature of the "%{crate}" crate.

%package     -n %{name}+error-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+error-devel

This package contains library source intended for building other packages which
use the "error" feature of the "%{crate}" crate.

%package     -n %{name}+from-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+from-devel

This package contains library source intended for building other packages which
use the "from" feature of the "%{crate}" crate.

%package     -n %{name}+from_str-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+from_str-devel

This package contains library source intended for building other packages which
use the "from_str" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+index-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+index-devel

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%package     -n %{name}+index_mut-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+index_mut-devel

This package contains library source intended for building other packages which
use the "index_mut" feature of the "%{crate}" crate.

%package     -n %{name}+into-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+into-devel

This package contains library source intended for building other packages which
use the "into" feature of the "%{crate}" crate.

%package     -n %{name}+into_iterator-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+into_iterator-devel

This package contains library source intended for building other packages which
use the "into_iterator" feature of the "%{crate}" crate.

%package     -n %{name}+is_variant-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+is_variant-devel

This package contains library source intended for building other packages which
use the "is_variant" feature of the "%{crate}" crate.

%package     -n %{name}+mul-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+mul-devel

This package contains library source intended for building other packages which
use the "mul" feature of the "%{crate}" crate.

%package     -n %{name}+mul_assign-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+mul_assign-devel

This package contains library source intended for building other packages which
use the "mul_assign" feature of the "%{crate}" crate.

%package     -n %{name}+not-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+not-devel

This package contains library source intended for building other packages which
use the "not" feature of the "%{crate}" crate.

%package     -n %{name}+sum-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+sum-devel

This package contains library source intended for building other packages which
use the "sum" feature of the "%{crate}" crate.

%package     -n %{name}+testing-helpers-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+testing-helpers-devel

This package contains library source intended for building other packages which
use the "testing-helpers" feature of the "%{crate}" crate.

%package     -n %{name}+try_from-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+try_from-devel

This package contains library source intended for building other packages which
use the "try_from" feature of the "%{crate}" crate.

%package     -n %{name}+try_into-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+try_into-devel

This package contains library source intended for building other packages which
use the "try_into" feature of the "%{crate}" crate.

%package     -n %{name}+try_unwrap-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+try_unwrap-devel

This package contains library source intended for building other packages which
use the "try_unwrap" feature of the "%{crate}" crate.

%package     -n %{name}+unwrap-devel
Summary:        Internal implementation of derive_more crate
BuildArch:      noarch
%description -n %{name}+unwrap-devel

This package contains library source intended for building other packages which
use the "unwrap" feature of the "%{crate}" crate.

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
%files -n rust-derive_more-impl-devel -f %{oreon_filedir}/rust-derive_more-impl-devel.list

%changelog

%autochangelog
