%global source0_hash 93edd9cd673087fa7518fd63ad6c87be2cd9b4e35034b1873f3e3258c018275b
%bcond check 1
%global debug_package %{nil}
%global crate libbpf-rs
Name:           rust-libbpf-rs0.24
Version:        0.24.8
Release:        1%{?dist}
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://crates.io/crates/libbpf-rs
Source0:        https://static.crates.io/crates/libbpf-rs/libbpf-rs-%{version}.crate
Patch:          libbpf-rs-fix-metadata.diff
Patch10:        libbpf-rs-disable-probe-tests-on-ppc64le-s390x.diff
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
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dont-generate-test-files-devel
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+dont-generate-test-files-devel

This package contains library source intended for building other packages which
use the "dont-generate-test-files" feature of the "%{crate}" crate.

%package     -n %{name}+generate-test-files-devel
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+generate-test-files-devel

This package contains library source intended for building other packages which
use the "generate-test-files" feature of the "%{crate}" crate.

%package     -n %{name}+libbpf-sys-devel
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+libbpf-sys-devel

This package contains library source intended for building other packages which
use the "libbpf-sys" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip :root:
    --skip test_object_build_from_memory
    --skip test_object_build_from_memory_empty_name
    --skip test_object_name
    --skip test_object_link_files
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libbpf-rs0.24-devel -f %{oreon_filedir}/rust-libbpf-rs0.24-devel.list

%changelog

%autochangelog
