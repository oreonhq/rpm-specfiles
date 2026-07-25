%global source0_hash 07bd130084fd4b1d87e7d24a1334eb31136e88fea83b0ab08ac05e1d9e033a2a

%bcond check 1
%global debug_package %{nil}

%global crate tpm2-policy

Name:           rust-%{crate}
Version:        0.6.0
Release:        %autorelease
Summary:        Specify and send TPM2 policies to satisfy object authorization

# Upstream license specification: EUPL-1.2
License:        EUPL-1.2
URL:            https://crates.io/crates/tpm2-policy
Source:         %{crates_source}
Patch0:         tpm2-policy-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Specify and send TPM2 policies to satisfy object authorization.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
