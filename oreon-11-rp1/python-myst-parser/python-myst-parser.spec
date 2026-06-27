%global source0_hash 472eacf90753abcd65739fd1b88f9eb41b14008968f53da23882c4331f36b2b6

%bcond_without check

Name:           python-myst-parser
Version:        4.0.1
Release:        1%{?dist}
Summary:        A commonmark compliant parser, with bridges to docutils and sphinx
License:        MIT
URL:            https://github.com/executablebooks/MyST-Parser
Source0:        https://github.com/executablebooks/MyST-Parser/archive/v%{version}/myst-parser-%{version}.tar.gz
Patch:          Adjust-test-output-to-docutils-0.22.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
A fully-functional markdown flavor and parser for Sphinx.}

%description %_description

%package -n     python3-myst-parser
Summary:        %{summary}

%description -n python3-myst-parser %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n MyST-Parser-%{version}
sed -i 's/docutils>=0\.19,<0\.22/docutils>=0.19/' pyproject.toml
sed -i '/"beautifulsoup4",/d' pyproject.toml
sed -i '/"coverage\[toml\]",/d' pyproject.toml
sed -i '/"defusedxml",/d' pyproject.toml
sed -i '/"pytest-cov",/d' pyproject.toml
sed -i '/"pytest-regressions",/d' pyproject.toml
sed -i '/"pytest-param-files/d' pyproject.toml
sed -i '/"sphinx-pytest",/d' pyproject.toml
sed -i '/"pygments<2.19",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files myst_parser

%if %{with check}
%check
%pyproject_check_import
%pytest -k "not test_sphinx_directives and not test_references_singlehtml and not test_extended_syntaxes and not test_includes and not test_fieldlist_extension"
%endif

%files -n python3-myst-parser -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/myst-anchors
%{_bindir}/myst-docutils-demo
%{_bindir}/myst-docutils-html
%{_bindir}/myst-docutils-html5
%{_bindir}/myst-docutils-latex
%{_bindir}/myst-docutils-xml
%{_bindir}/myst-docutils-pseudoxml
%{_bindir}/myst-inv

%changelog
%autochangelog
