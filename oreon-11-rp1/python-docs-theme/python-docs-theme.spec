%global source0_hash ade77cc5731fbb45e47fd68c8ef83e048bc53990b37ba74445d16ba1731c313f

Name:           python-docs-theme
Version:        2026.9
Release:        %autorelease
Summary:        The Sphinx theme for the CPython docs and related projects

License:        PSF-2.0
URL:            https://github.com/python/python-docs-theme/
Source: https://codeload.github.com/python/python-docs-theme/tar.gz/refs/tags/2026.9
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description Python Docs Sphinx Theme is the theme for the Python documentation.

%description
%_description

%package -n     python3-docs-theme
Summary:        %{summary}

%description -n python3-docs-theme
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files python_docs_theme

%files -n python3-docs-theme -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
