%global source0_hash 835169da0173ea373ddf5987632aac1f918967fbbe58195e304342282efa6089
%bcond check 1
%global debug_package %{nil}
%global crate version-sync
Name:           rust-version-sync
Version:        0.9.5
Release:        1%{?dist}
Summary:        Crate for ensuring that version numbers in README files and other fil...
License:        MIT
URL:            https://crates.io/crates/version-sync
Source0:        https://static.crates.io/crates/version-sync/version-sync-%{version}.crate
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
Summary:        Crate for ensuring that version numbers in README files and other fil...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+contains_regex-devel
Summary:        Crate for ensuring that version numbers in README files and other fil...
BuildArch:      noarch
%description -n %{name}+contains_regex-devel

This package contains library source intended for building other packages which
use the "contains_regex" feature of the "%{crate}" crate.

%package     -n %{name}+html_root_url_updated-devel
Summary:        Crate for ensuring that version numbers in README files and other fil...
BuildArch:      noarch
%description -n %{name}+html_root_url_updated-devel

This package contains library source intended for building other packages which
use the "html_root_url_updated" feature of the "%{crate}" crate.

%package     -n %{name}+markdown_deps_updated-devel
Summary:        Crate for ensuring that version numbers in README files and other fil...
BuildArch:      noarch
%description -n %{name}+markdown_deps_updated-devel

This package contains library source intended for building other packages which
use the "markdown_deps_updated" feature of the "%{crate}" crate.

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
%files -n rust-version-sync-devel -f %{oreon_filedir}/rust-version-sync-devel.list

%changelog

%autochangelog
