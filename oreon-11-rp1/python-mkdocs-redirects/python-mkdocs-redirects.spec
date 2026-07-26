%global source0_hash 9420066d70e2a6bb357adf86e67023dcdca1857f97f07c7fe450f8f1fb42f861

Name:           python-mkdocs-redirects
Version:        1.2.1
Release:        %autorelease
Summary:        MkDocs plugin for dynamic page redirects to prevent broken links
BuildArch:      noarch

License:        MIT
URL:            https://github.com/datarobot/mkdocs-redirects
Source:         %{pypi_source mkdocs-redirects}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
A MkDocs plugin for dynamic page redirects to prevent broken links.

%package -n python3-mkdocs-redirects
Summary:        %{summary}

%description -n python3-mkdocs-redirects
A MkDocs plugin for dynamic page redirects to prevent broken links.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs-redirects-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%pyproject_save_files mkdocs_redirects

%files -n python3-mkdocs-redirects -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
