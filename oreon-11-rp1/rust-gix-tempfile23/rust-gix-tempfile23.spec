%global source0_hash 6ef60812443484e67bf84e444cc71b4c78ae62deb822221774a4fa0c57fdb17f
%bcond check 0
%global debug_package %{nil}
%global crate gix-tempfile
Name:           rust-gix-tempfile23
Version:        23.0.2
Release:        1%{?dist}
Summary:        A tempfile implementation with a global registry to assure cleanup
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-tempfile
Source0:        https://static.crates.io/crates/gix-tempfile/gix-tempfile-%{version}.crate
Patch:          gix-tempfile-fix-metadata-auto.diff
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
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+hp-hashmap-devel
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+hp-hashmap-devel

This package contains library source intended for building other packages which
use the "hp-hashmap" feature of the "%{crate}" crate.

%package     -n %{name}+signal-hook-devel
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+signal-hook-devel

This package contains library source intended for building other packages which
use the "signal-hook" feature of the "%{crate}" crate.

%package     -n %{name}+signal-hook-registry-devel
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+signal-hook-registry-devel

This package contains library source intended for building other packages which
use the "signal-hook-registry" feature of the "%{crate}" crate.

%package     -n %{name}+signals-devel
Summary:        A tempfile implementation with a global registry to assure cleanup
BuildArch:      noarch
%description -n %{name}+signals-devel

This package contains library source intended for building other packages which
use the "signals" feature of the "%{crate}" crate.

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
%files -n rust-gix-tempfile23-devel -f %{oreon_filedir}/rust-gix-tempfile23-devel.list

%changelog

%autochangelog
