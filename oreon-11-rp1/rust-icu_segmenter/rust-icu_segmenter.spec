%global source0_hash 82d07aafccd67af15d02512a6adf5896fbc5ed00f2e99b471d2efa14016db3db
%bcond check 1
%global debug_package %{nil}
%global crate icu_segmenter
Name:           rust-icu_segmenter
Version:        2.3.0
Release:        1%{?dist}
Summary:        Unicode line breaking and text segmentation algorithms
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_segmenter
Source0:        https://static.crates.io/crates/icu_segmenter/icu_segmenter-%{version}.crate
Patch:          icu_segmenter-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Unicode line breaking and text segmentation algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+auto-devel
Summary:        Unicode line breaking and text segmentation algorithms
BuildArch:      noarch
%description -n %{name}+auto-devel

This package contains library source intended for building other packages which
use the "auto" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        Unicode line breaking and text segmentation algorithms
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        Unicode line breaking and text segmentation algorithms
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+lstm-devel
Summary:        Unicode line breaking and text segmentation algorithms
BuildArch:      noarch
%description -n %{name}+lstm-devel

This package contains library source intended for building other packages which
use the "lstm" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Unicode line breaking and text segmentation algorithms
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml str dev-dependencies.icu_properties.version '~%{version}'
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib
%cargo_test -- --test cnn
%cargo_test -- --test complex_word
%cargo_test -- --test css_line_break
%cargo_test -- --test locale
%cargo_test -- --test spec_test
%cargo_test -- --test word_rule_status
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_segmenter-devel -f %{oreon_filedir}/rust-icu_segmenter-devel.list

%changelog

%autochangelog
