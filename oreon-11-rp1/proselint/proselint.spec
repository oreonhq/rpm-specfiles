%global source0_hash 624964272bea14767e5df2561d87dd30767938c8cb52fb23585bc37580680e86

Name:           proselint
Version:        0.14.0
Release:        %autorelease
Summary:        A linter for English prose

License:        BSD-3-Clause
URL:            https://github.com/amperser/proselint
Source0:        %pypi_source
BuildArch:      noarch

Requires:       python3-click
Requires:       python3-six

BuildRequires:  python3-devel

# For running the tests:
BuildRequires:  python3-click
BuildRequires:  python3-pytest
BuildRequires:  python3-six

%description
proselint's goal is to aggregate knowledge about best practices in
writing and to make that knowledge immediately accessible to all authors
in the form of a linter for prose.  It is a command-line utility that
can be integrated into existing tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%pytest

%files -f %{pyproject_files}
%{_bindir}/%{name}

%changelog
%autochangelog
