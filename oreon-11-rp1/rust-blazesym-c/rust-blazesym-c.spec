%global source0_hash f09c03df5c33f265a7ae6de11a81c9ebb69c4ca632afa45e9fcf7a96c1d8cca0
%bcond check 1
%global binary_license BSD-3-Clause AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Zlib OR Apache-2.0)
%global crate blazesym-c
%global crate_version 0.1.0-rc.0
Name:           rust-blazesym-c
Version:        0.1.10
Release:        1%{?dist}
Summary:        C bindings for blazesym
License:        BSD-3-Clause
URL:            https://crates.io/crates/blazesym-c
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          blazesym-c-fix-metadata.diff
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}-libs
Summary:        C bindings for blazesym
License:        %{binary_license}
%description -n %{crate}-libs

%package     -n %{crate}-devel
Summary:        C bindings for blazesym
License:        %{binary_license}
Requires:       %{crate}-libs%{?_isa} = %{version}-%{release}
%description -n %{crate}-devel

The %{crate}-devel package contains libraries and header files for
developing applications that use %{crate}.

%package     -n %{crate}-static
Summary:        C bindings for blazesym
License:        %{binary_license}
Requires:       %{crate}-devel%{?_isa} = %{version}-%{release}
%description -n %{crate}-static

The %{crate}-static package contains library files for
developing static applications that use %{crate}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        C bindings for blazesym
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+check-doc-snippets-devel
Summary:        C bindings for blazesym
BuildArch:      noarch
%description -n %{name}+check-doc-snippets-devel

This package contains library source intended for building other packages which
use the "check-doc-snippets" feature of the "%{crate}" crate.

%package     -n %{name}+generate-c-header-devel
Summary:        C bindings for blazesym
BuildArch:      noarch
%description -n %{name}+generate-c-header-devel

This package contains library source intended for building other packages which
use the "generate-c-header" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%cargo_cbuild
%install
%cargo_install
%cargo_cinstall
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip inspect::tests::lookup_dwarf
    --skip normalize::tests::normalize_build_id_reading
    --skip symbolize::tests::symbolize_configurable_debug_dirs
    --skip symbolize::tests::symbolize_no_debug_dirs
    --skip symbolize::tests::symbolize_elf_file_offset
    --skip symbolize::tests::symbolize_dwarf_demangle
    --skip normalize::tests::normalize_user_addrs_sorted
    --skip normalize::tests::normalize_user_addrs
    --skip symbolize::tests::symbolize_elf_dwarf_gsym
    --skip normalize::tests::normalize_user_addrs_unsorted_failure
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n blazesym-c-libs -f %{oreon_filedir}/blazesym-c-libs.list
%files -n blazesym-c-devel -f %{oreon_filedir}/blazesym-c-devel.list
%files -n blazesym-c-static -f %{oreon_filedir}/blazesym-c-static.list
%files -n rust-blazesym-c-devel -f %{oreon_filedir}/rust-blazesym-c-devel.list

%changelog

%autochangelog
