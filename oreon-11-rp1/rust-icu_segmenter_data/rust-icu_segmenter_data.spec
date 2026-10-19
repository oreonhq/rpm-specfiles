%global source0_hash ae293c039020f9ec10710af98d29ce6aa2051486638b49c9a6409f3b4a9e98ad
%bcond check 1
%global debug_package %{nil}
%global crate icu_segmenter_data
Name:           rust-icu_segmenter_data
Version:        2.3.0
Release:        1%{?dist}
Summary:        Data for the icu_segmenter crate
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_segmenter_data
Source0:        https://static.crates.io/crates/icu_segmenter_data/icu_segmenter_data-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

# The data in this package has been “baked” into Rust code using the
# icu_datagen crate, which is built on top of the databake crate. For
# guidelines compliance purpose, we consider these files to have more
# properties of data than of generated code. For example, other than the static
# byte buffers encoding the data, all of the Rust source code is boilerplate
# produced by icu_datagen; it has no “original sources” outside of icu_datagen
# in any meaningful sense, other than the original form of the Unicode data
# itself, which is ultimately attributable to the CLDR
# (https://github.com/unicode-org/cldr-json/) and/or the data files shipped
# with ICU (https://github.com/unicode-org/icu/). Further details, discussion,
# and rationale appear in https://bugzilla.redhat.com/show_bug.cgi?id=2358292.

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Data for the icu_segmenter crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-icu_segmenter_data-devel -f %{oreon_filedir}/rust-icu_segmenter_data-devel.list

%changelog

%autochangelog
