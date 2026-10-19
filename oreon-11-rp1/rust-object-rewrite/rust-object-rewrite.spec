%global source11_hash 0b74dfa0bcee5c420c6b7f67b4b2658f9ab8388c97b8e733975f2cecbdd668a6
%global source10_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash 52e4dced2f5855818213523f9c8f75f2c07495f57c585fc402d14dfe5361d18d
%bcond check 1
%global crate object-rewrite
Name:           rust-object-rewrite
Version:        0.1.1
Release:        1%{?dist}
Summary:        Rewrite object files with modifications
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/object-rewrite
Source0:        https://static.crates.io/crates/object-rewrite/object-rewrite-%{version}.crate
Source10:       https://github.com/gimli-rs/object/raw/refs/tags/rewrite-%{version}/LICENSE-APACHE
Source11:       https://github.com/gimli-rs/object/raw/refs/tags/rewrite-%{version}/LICENSE-MIT
Patch:          object-rewrite-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Rewrite object files with modifications
License:        %{shrink:
    (Apache-2.0 OR MIT) AND
    MIT AND
    Zlib AND
    (Unlicense OR MIT)
    }
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rewrite object files with modifications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Rewrite object files with modifications
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Rewrite object files with modifications
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        Rewrite object files with modifications
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Rewrite object files with modifications
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' '%{SOURCE11}' .
%oreon_vendor_cargo
%build

%cargo_build -f cli
%{cargo_license_summary -f cli}
%{cargo_license -f cli} > LICENSE.dependencies
help2man --no-info --name='%{summary}' --output=object-rewrite.1 \
    target/rpm/object-rewrite
%install
%cargo_install -f cli
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 object-rewrite.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f cli
%endif
%files -f %{oreon_filedir}/main.list
%files -n object-rewrite -f %{oreon_filedir}/object-rewrite.list
%files -n rust-object-rewrite-devel -f %{oreon_filedir}/rust-object-rewrite-devel.list

%changelog

%autochangelog
