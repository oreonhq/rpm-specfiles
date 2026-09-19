%global source0_hash 62d6408d1406657be2f9d1701fbae379331d30d2f6e92050710edb0d34eeb480
%global debug_package %{nil}
%bcond check 1

%global crate test-strategy

Name:           rust-test-strategy0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Procedural macro to easily write higher-order strategies in proptest

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/test-strategy
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Procedural macro to easily write higher-order strategies in proptest.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
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

%autosetup -n %{crate}-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
