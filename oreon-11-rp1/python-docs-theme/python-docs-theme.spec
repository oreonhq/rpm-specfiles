%global source0_hash b540b6bd4f88682840d52fcfaf55281bb8a5203abe388353bae9d3b0defeb5ae

BuildRequires:  /usr/bin/pybabel
Name:           python-docs-theme
Version:        2026.9.1
Release:        %autorelease
Summary:        The Sphinx theme for the CPython docs and related projects

License:        PSF-2.0
URL:            https://github.com/python/python-docs-theme/
Source:         %{url}archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3dist(babel)
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
