%global source0_hash b4aeaa1f2460f1d348eeaeed86aea999ce98c1bded6f089ff8514c9d9dbdc973
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate protobuf-parse
Name:           rust-protobuf-parse
Version:        3.7.2
Release:        1%{?dist}
Summary:        Parse .proto files
License:        MIT AND BSD-3-Clause
URL:            https://crates.io/crates/protobuf-parse
Source0:        https://static.crates.io/crates/protobuf-parse/protobuf-parse-%{version}.crate
Patch:          protobuf-parse-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/protoc
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       /usr/bin/protoc
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Parse .proto files
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

%{cargo_test -- -- --exact %{shrink:
    --skip test_against_protobuf_protos::test
    --skip test_bundled_google_proto_files_consistent
    --skip test_bundled_rustproto_proto_consistent
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-protobuf-parse-devel -f %{oreon_filedir}/rust-protobuf-parse-devel.list

%changelog

%autochangelog
