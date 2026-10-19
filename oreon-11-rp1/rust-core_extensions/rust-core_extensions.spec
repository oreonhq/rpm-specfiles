%global source0_hash 42bb5e5d0269fd4f739ea6cedaf29c16d81c27a7ce7582008e90eb50dcd57003
%bcond check 0
%global debug_package %{nil}
%global crate core_extensions
Name:           rust-core_extensions
Version:        1.5.4
Release:        1%{?dist}
Summary:        Extensions for core/std library types, and other miscelaneous features.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/core_extensions
Source0:        https://static.crates.io/crates/core_extensions/core_extensions-%{version}.crate
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

%package     -n %{name}+__test-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+__test-devel

This package contains library source intended for building other packages which
use the "__test" feature of the "%{crate}" crate.

%package     -n %{name}+__test_older-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+__test_older-devel

This package contains library source intended for building other packages which
use the "__test_older" feature of the "%{crate}" crate.

%package     -n %{name}+all_items-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+all_items-devel

This package contains library source intended for building other packages which
use the "all_items" feature of the "%{crate}" crate.

%package     -n %{name}+all_items_no_derive-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+all_items_no_derive-devel

This package contains library source intended for building other packages which
use the "all_items_no_derive" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+bools-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+bools-devel

This package contains library source intended for building other packages which
use the "bools" feature of the "%{crate}" crate.

%package     -n %{name}+callable-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+callable-devel

This package contains library source intended for building other packages which
use the "callable" feature of the "%{crate}" crate.

%package     -n %{name}+collections-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+collections-devel

This package contains library source intended for building other packages which
use the "collections" feature of the "%{crate}" crate.

%package     -n %{name}+const_default-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+const_default-devel

This package contains library source intended for building other packages which
use the "const_default" feature of the "%{crate}" crate.

%package     -n %{name}+const_val-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+const_val-devel

This package contains library source intended for building other packages which
use the "const_val" feature of the "%{crate}" crate.

%package     -n %{name}+core_extensions_proc_macros-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+core_extensions_proc_macros-devel

This package contains library source intended for building other packages which
use the "core_extensions_proc_macros" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+enable_proc_macro_crate-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+enable_proc_macro_crate-devel

This package contains library source intended for building other packages which
use the "enable_proc_macro_crate" feature of the "%{crate}" crate.

%package     -n %{name}+generics_parsing-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+generics_parsing-devel

This package contains library source intended for building other packages which
use the "generics_parsing" feature of the "%{crate}" crate.

%package     -n %{name}+integers-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+integers-devel

This package contains library source intended for building other packages which
use the "integers" feature of the "%{crate}" crate.

%package     -n %{name}+item_parsing-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+item_parsing-devel

This package contains library source intended for building other packages which
use the "item_parsing" feature of the "%{crate}" crate.

%package     -n %{name}+iterators-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+iterators-devel

This package contains library source intended for building other packages which
use the "iterators" feature of the "%{crate}" crate.

%package     -n %{name}+macro_utils-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+macro_utils-devel

This package contains library source intended for building other packages which
use the "macro_utils" feature of the "%{crate}" crate.

%package     -n %{name}+marker_type-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+marker_type-devel

This package contains library source intended for building other packages which
use the "marker_type" feature of the "%{crate}" crate.

%package     -n %{name}+on_drop-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+on_drop-devel

This package contains library source intended for building other packages which
use the "on_drop" feature of the "%{crate}" crate.

%package     -n %{name}+option_result-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+option_result-devel

This package contains library source intended for building other packages which
use the "option_result" feature of the "%{crate}" crate.

%package     -n %{name}+phantom-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+phantom-devel

This package contains library source intended for building other packages which
use the "phantom" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_46-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+rust_1_46-devel

This package contains library source intended for building other packages which
use the "rust_1_46" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_51-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+rust_1_51-devel

This package contains library source intended for building other packages which
use the "rust_1_51" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_59-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+rust_1_59-devel

This package contains library source intended for building other packages which
use the "rust_1_59" feature of the "%{crate}" crate.

%package     -n %{name}+rust_latest_stable-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+rust_latest_stable-devel

This package contains library source intended for building other packages which
use the "rust_latest_stable" feature of the "%{crate}" crate.

%package     -n %{name}+self_ops-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+self_ops-devel

This package contains library source intended for building other packages which
use the "self_ops" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+serde_-devel

This package contains library source intended for building other packages which
use the "serde_" feature of the "%{crate}" crate.

%package     -n %{name}+slices-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+slices-devel

This package contains library source intended for building other packages which
use the "slices" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+strings-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+strings-devel

This package contains library source intended for building other packages which
use the "strings" feature of the "%{crate}" crate.

%package     -n %{name}+track_caller-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+track_caller-devel

This package contains library source intended for building other packages which
use the "track_caller" feature of the "%{crate}" crate.

%package     -n %{name}+transparent_newtype-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+transparent_newtype-devel

This package contains library source intended for building other packages which
use the "transparent_newtype" feature of the "%{crate}" crate.

%package     -n %{name}+type_asserts-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+type_asserts-devel

This package contains library source intended for building other packages which
use the "type_asserts" feature of the "%{crate}" crate.

%package     -n %{name}+type_identity-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+type_identity-devel

This package contains library source intended for building other packages which
use the "type_identity" feature of the "%{crate}" crate.

%package     -n %{name}+type_level_bool-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+type_level_bool-devel

This package contains library source intended for building other packages which
use the "type_level_bool" feature of the "%{crate}" crate.

%package     -n %{name}+void-devel
Summary:        Extensions for core/std library types, and other miscelaneous features.
BuildArch:      noarch
%description -n %{name}+void-devel

This package contains library source intended for building other packages which
use the "void" feature of the "%{crate}" crate.

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
%files -n rust-core_extensions-devel -f %{oreon_filedir}/rust-core_extensions-devel.list

%changelog

%autochangelog
