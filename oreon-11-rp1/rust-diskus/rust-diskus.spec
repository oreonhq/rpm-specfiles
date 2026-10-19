%global source0_hash ec07379c016f78e7ddcd953663b9ed17928ff384928d34d824ed7e463bd3d908
%bcond check 1
%global crate diskus
Name:           rust-diskus
Version:        0.9.0
Release:        1%{?dist}
Summary:        Minimal, fast alternative to 'du -sh'
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/diskus
Source0:        https://static.crates.io/crates/diskus/diskus-%{version}.crate
Patch:          diskus-fix-metadata.diff
Patch10:        diskus-0.9.0-tempdir-tempfile.patch
Patch11:        https://github.com/sharkdp/diskus/pull/60.patch
Patch12:        diskus-0.9.0-no-atty.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Minimal, fast alternative to 'du -sh'
License:        %{shrink:
    (MIT OR Apache-2.0) AND
    MIT AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    }
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Minimal, fast alternative to 'du -sh'
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Minimal, fast alternative to 'du -sh'
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 doc/diskus.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n diskus -f %{oreon_filedir}/diskus.list
%files -n rust-diskus-devel -f %{oreon_filedir}/rust-diskus-devel.list

%changelog

%autochangelog
