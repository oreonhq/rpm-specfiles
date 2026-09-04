%global source0_hash 5202d9cf41b2ca3a4ab51a4fb700a3ec6b95b9c0fa020a6807a5839fa7e57aa7

# NOTE: Building documentation requires python-sphinx-book-theme, which
# introduces a circular dependency: python-linkify-it-py ->
# python-sphinx-book-theme -> myst-nb -> python-myst-parser ->
# python-linkify-it-py

%global giturl  https://github.com/tsutsu3/linkify-it-py

Name:           python-linkify-it-py
Version:        2.2.0
Release:        %autorelease
Summary:        Link recognition library with full Unicode support

License:        MIT
URL:            https://linkify-it-py.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/linkify-it-py-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install): -l linkify_it

%global _description %{expand:This is a Python port of linkify-it [1], a link recognition library with FULL
unicode support.  It is focused on high quality link pattern detection in
plain text.  See a JavaScript demo [2].

References:
[1] https://github.com/markdown-it/linkify-it
[2] https://markdown-it.github.io/linkify-it/}

%description
%_description

%package     -n python3-linkify-it-py
Summary:        Link recognition library with full Unicode support

%description -n python3-linkify-it-py
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n linkify-it-py-%{version}

# Do not run coverage tools in RPM builds
sed -i 's/, "coverage", "pytest-cov"//' pyproject.toml

%check
%pytest -v

%files -n python3-linkify-it-py -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
