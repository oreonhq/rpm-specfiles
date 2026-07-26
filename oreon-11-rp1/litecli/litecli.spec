%global source0_hash 3285997f57b2d72dc70e9856cb302cddd8de07b0cebf5c90a60ecd20a053cd79

Name:           litecli
Version:        1.15.0
Release:        %autorelease
Summary:        CLI for SQLite Databases with auto-completion and syntax highlighting
License:        BSD-3-Clause
URL:            https://litecli.com
BuildArch:      noarch
Source:         %{pypi_source litecli}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Previously the Python library was split off to it's own subpackage.  The
# upstream only supports this as a CLI, not a library.
Obsoletes:      python3-litecli < 1.9.0-12
Provides:       python3-litecli = %{version}-%{release}

%description
A command-line client for SQLite databases that has auto-completion and syntax
highlighting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l litecli

%check
# skip tests that require llm
%pytest --verbose \
    --ignore tests/test_llm_special.py \
    tests

%files -f %{pyproject_files}
%{_bindir}/litecli

%changelog
%autochangelog
