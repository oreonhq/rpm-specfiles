%global source0_hash 65731e1e4ec6d719693e24fee9340f5516460b2b7244d2a89bed4ce3cfa6a173

Name:           python-mkdocs-static-i18n
Version:        1.3.0
Release:        %autorelease
Summary:        MkDocs i18n plugin using static translation Markdown files

License:        MIT
URL:            https://ultrabug.github.io/mkdocs-static-i18n/
Source:         %{pypi_source mkdocs_static_i18n}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
The mkdocs-static-i18n plugin allows you to support multiple languages of your
documentation by adding static translation files to your existing documentation
pages.}

%description %_description

%package -n     python3-mkdocs-static-i18n
Summary:        %{summary}

%description -n python3-mkdocs-static-i18n %_description

%pyproject_extras_subpkg -n python3-mkdocs-static-i18n material

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs_static_i18n-%{version}

%generate_buildrequires
%pyproject_buildrequires -x material

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_static_i18n

%check
%pytest -v

%files -n python3-mkdocs-static-i18n -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
