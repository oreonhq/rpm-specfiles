%global source0_hash cc999ba15a3ce2a46eab35fcaabea9907f5c74bc49e79d9c866b51d4b0fa7f33

%bcond tests 1

Name:           mkdocs-bootswatch
Version:        1.1
Release:        13%{?dist}
Summary:        Bootswatch themes for MkDocs

License:        BSD-2-Clause AND MIT
URL:            http://mkdocs.github.io/mkdocs-bootswatch
Source:         %{pypi_source mkdocs-bootswatch}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs-bootswatch-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_bootswatch

%check
%pyproject_check_import

%if %{with tests}
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
for theme_dir in ../mkdocs_bootswatch/*; do
    if [ -d $theme_dir ]; then
       mkdocs build --theme $(basename $theme_dir)
    fi
done
popd
%endif

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
