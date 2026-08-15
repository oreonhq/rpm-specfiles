%global source0_hash faa67bab9ff362228eb3d00bd024a4965d8231bbb7921167f0cfa66c6626b225

%bcond check 1
%global debug_package %{nil}

%global crate handlebars

Name:           rust-handlebars4
Version:        4.5.0
Release:        %autorelease
Summary:        Handlebars templating implemented in Rust

License:        MIT
URL:            https://crates.io/crates/handlebars
Source:         %{crates_source}
Patch:          handlebars-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Handlebars templating implemented in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+dir_source-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dir_source-devel %{_description}

This package contains library source intended for building other packages which
use the "dir_source" feature of the "%{crate}" crate.

%files       -n %{name}+dir_source-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_logging-devel %{_description}

This package contains library source intended for building other packages which
use the "no_logging" feature of the "%{crate}" crate.

%files       -n %{name}+no_logging-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+script_helper-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+script_helper-devel %{_description}

This package contains library source intended for building other packages which
use the "script_helper" feature of the "%{crate}" crate.

%files       -n %{name}+script_helper-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+string_helpers-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+string_helpers-devel %{_description}

This package contains library source intended for building other packages which
use the "string_helpers" feature of the "%{crate}" crate.

%files       -n %{name}+string_helpers-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{crate}-%{version} -p1
%cargo_prep
rm examples/dev_mode.rs

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
