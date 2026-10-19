%global source0_hash ed7e41e369d8ec9be6e141d0cf10091e198bc9de40447d81057dcb326cb70351
%bcond check 1
%global cargo_install_lib 0
%global crate wiremix
Name:           rust-wiremix
Version:        0.11.0
Release:        1%{?dist}
Summary:        TUI mixer for PipeWire
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wiremix
Source0:        https://static.crates.io/crates/wiremix/wiremix-%{version}.crate
Patch:          wiremix-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        TUI mixer for PipeWire
License:        %{shrink:
    (MIT OR Apache-2.0) AND
    MIT AND
    Unicode-DFS-2016 AND
    Zlib AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
help2man --no-info --name='%{summary}' --output=wiremix.1 target/rpm/wiremix
%install
%cargo_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 wiremix.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n wiremix -f %{oreon_filedir}/wiremix.list

%changelog

%autochangelog
