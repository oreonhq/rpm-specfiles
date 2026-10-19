%global source0_hash e660451e55124f798a69a5af3f49ccfbefbd41910eefd25caf2393e1f3473ec1
%bcond check 0
%global debug_package %{nil}
%global crate quick-xml
Name:           rust-quick-xml
Version:        0.41.0
Release:        1%{?dist}
Summary:        High performance xml reader and writer
License:        MIT
URL:            https://crates.io/crates/quick-xml
Source0:        https://static.crates.io/crates/quick-xml/quick-xml-%{version}.crate
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
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+async-tokio-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+async-tokio-devel

This package contains library source intended for building other packages which
use the "async-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+encoding-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+encoding-devel

This package contains library source intended for building other packages which
use the "encoding" feature of the "%{crate}" crate.

%package     -n %{name}+encoding_rs-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+encoding_rs-devel

This package contains library source intended for building other packages which
use the "encoding_rs" feature of the "%{crate}" crate.

%package     -n %{name}+escape-html-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+escape-html-devel

This package contains library source intended for building other packages which
use the "escape-html" feature of the "%{crate}" crate.

%package     -n %{name}+overlapped-lists-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+overlapped-lists-devel

This package contains library source intended for building other packages which
use the "overlapped-lists" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-types-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+serde-types-devel

This package contains library source intended for building other packages which
use the "serde-types" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        High performance xml reader and writer
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-quick-xml-devel -f %{oreon_filedir}/rust-quick-xml-devel.list

%changelog

%autochangelog
