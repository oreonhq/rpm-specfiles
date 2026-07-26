%global source0_hash 52022dc14dcc0451e05e54a8f5d5e7760351b6701eff816d1e9739577ec5635e

%bcond tests 1

Name:           python-mkdocs-gen-files
Version:        0.6.0
Release:        %autorelease
Summary:        MkDocs plugin to generate documentation pages during the build

License:        MIT
URL:            https://oprypin.github.io/mkdocs-gen-files
Source:         %{pypi_source mkdocs_gen_files}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-golden)
%endif

%global _description %{expand:
This package provides a plugin for MkDocs to programmatically generate
documentation pages during the build.}

%description %_description

%package -n     python3-mkdocs-gen-files
Summary:        %{summary}

%description -n python3-mkdocs-gen-files %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs_gen_files-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_gen_files

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-gen-files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
