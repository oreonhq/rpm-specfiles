%global source0_hash 331e0d0c9c3459fad3c1a317c08ebc2de3ee97ced1bcc0cce0b8d8848da43f58

Name:           rpm-spec-language-server
Version:        0.0.2
Release:        2%{?dist}
Summary:        Language Server for RPM spec files

License:        GPL-2.0-or-later
URL:            https://github.com/dcermak/rpm-spec-language-server
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-typeguard

%description
This is a server implementing the Language Server Protocol for RPM Spec files.

Supported LSP endpoints:

- Autocompletion of macro names, spec sections and preamble keywords
- Jump to macro definition
- Expand macros on hover
- Breadcrumbs/document sections

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Relax poetry dependencies
sed -i 's/pygls = "^2.0"/pygls = "*"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'rpm_spec_language_server'

%check
# Some tests are failing
# See https://github.com/dcermak/rpm-spec-language-server/issues/455#issuecomment-3429420682
%pytest \
    --deselect tests/test_extract_docs.py::test_fetch_upstream_spec_md \
    --deselect tests/test_extract_docs.py::test_parse_upstream_spec_md \
    --deselect tests/test_extract_docs.py::test_cache_creation \
    --deselect tests/test_extract_docs.py::test_spec_md_fetched_from_upstream_if_not_in_rpm_package

%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/rpm_lsp_server

%changelog
%autochangelog
