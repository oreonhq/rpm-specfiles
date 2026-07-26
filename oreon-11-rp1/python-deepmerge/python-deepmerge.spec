%global source0_hash 5c3d86081fbebd04dd5de03626a0607b809a98fb6ccba5770b62466fe940ff20

Name:           python-deepmerge
Version:        2.0
Release:        5%{?dist}
Summary:        Toolset for deeply merging Python dictionaries

License:        MIT
URL:            http://deepmerge.readthedocs.io/en/latest/
Source:         %{pypi_source deepmerge}

BuildArch:      noarch
BuildRequires:  python3-devel
# Not using auto dev deps to avoid unwanted style and lint dependencies
BuildRequires:  python3-pytest

%global _description \
%{summary}.

%description %_description

%package -n     python3-deepmerge
Summary:        %{summary}

%description -n python3-deepmerge %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n deepmerge-%{version}

# Move tests out of the package path
mv deepmerge/tests tests

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l deepmerge

%check
%pyproject_check_import
%pytest

%files -n python3-deepmerge -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
