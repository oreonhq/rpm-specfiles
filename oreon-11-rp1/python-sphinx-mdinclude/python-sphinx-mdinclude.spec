%global source0_hash 447462e82cb8be61404a2204227f920769eb923d2f57608e3325f3bb88286b4c

%global srcname sphinx_mdinclude
%global distname sphinx-mdinclude

%global _description %{expand:
sphinx-mdinclude is a simple Sphinx extension that enables including Markdown
documents from within reStructuredText. It provides the `.. mdinclude::`
directive, and automatically converts the content of Markdown documents to
reStructuredText format.}

Name:           python-%{distname}
Version:        0.6.2
Release:        %autorelease
Summary:        Markdown extension for Sphinx

License:        MIT
URL:            https://github.com/omnilib/sphinx-mdinclude
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{_description}

%package -n     python3-%{distname}
Summary:        %{summary}
Requires:       python3dist(sphinx)

%description -n python3-%{distname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest -v

%files -n python3-%{distname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
