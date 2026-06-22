%global source0_hash a458fad2489698dd392a624551644975b01f5684bd7721e09999fd37e0f26e91

%bcond check 1

%ifarch %{ix86}
%global rustflags_debuginfo 1
%endif

%global crate cargo-c
%global crate_version 0.10.21+cargo-0.95.0

Name:           rust-cargo-c
Version:        0.10.21
Release:        1%{?dist}
Summary:        Helper program to build and install c-like libraries

License:        MIT
URL:            https://crates.io/crates/cargo-c
Source0:        https://static.crates.io/crates/cargo-c/cargo-c-%{crate_version}.crate
Source1:        macros.cargo-c
Patch:          cargo-c-fix-metadata-auto.diff
Patch:          cargo-c-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Helper program to build and install c-like libraries.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        %{shrink:
    MIT AND
    AND Apache-2.0
    AND BSD-2-Clause
    AND BSD-3-Clause
    AND ISC
    AND MPL-2.0
    AND Unicode-3.0
    AND Unicode-DFS-2016
    AND Zlib
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (MIT OR Apache-2.0 OR BSD-1-Clause)
    AND (MIT OR Apache-2.0 OR Zlib)
    AND (MIT-0 OR Apache-2.0)
    AND (Unlicense OR MIT)
}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/cargo-capi
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall
%{_bindir}/cargo-ctest
%{_rpmmacrodir}/macros.cargo-c
Provides:       cargo-c = %{version}-%{release}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} %{SOURCE1}

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
