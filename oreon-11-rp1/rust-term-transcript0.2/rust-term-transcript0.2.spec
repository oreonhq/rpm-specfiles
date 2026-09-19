%global source0_hash 6d77280c9041d978e4ffedbdd19f710a1360085510c5e99dbcfec8e2f2bd4285
%global debug_package %{nil}
%bcond check 1

%global crate term-transcript

Name:           rust-term-transcript0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Snapshotting and snapshot testing for CLI / REPL applications

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/term-transcript
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Snapshotting and snapshot testing for CLI / REPL applications.}

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
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+svg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+svg-devel %{_description}

This package contains library source intended for building other packages which
use the "svg" feature of the "%{crate}" crate.

%files       -n %{name}+svg-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%files       -n %{name}+test-devel
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
