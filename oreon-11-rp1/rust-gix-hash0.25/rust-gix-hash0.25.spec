%global source0_hash cb0926d3819c837750b4e03c7754901e73f68b8c9b690753a6372a1bed4eedce
%bcond check 0
%global debug_package %{nil}
%global crate gix-hash
Name:           rust-gix-hash0.25
Version:        0.25.1
Release:        1%{?dist}
Summary:        Borrowed and owned git hash digests used to identify git objects
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-hash
Source0:        https://static.crates.io/crates/gix-hash/gix-hash-%{version}.crate
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
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-checked-devel
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+sha1-checked-devel

This package contains library source intended for building other packages which
use the "sha1-checked" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Borrowed and owned git hash digests used to identify git objects
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

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
%files -n rust-gix-hash0.25-devel -f %{oreon_filedir}/rust-gix-hash0.25-devel.list

%changelog

%autochangelog
