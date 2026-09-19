%global source0_hash a6b7b0b6df0a380783ce5b29150c2d30352746f027a3e294d37183995d3f23ed

%global srcname sphinx-autodoc-typehints
%global altname sphinx_autodoc_typehints

%global common_description %{expand:
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.}

Name:           python-%{srcname}
Version:        3.1.0
Release:        %autorelease
Summary:        Type hints support for the Sphinx autodoc extension

License:        MIT
URL:            https://github.com/tox-dev/sphinx-autodoc-typehints
Source0:        %{pypi_source %{altname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{altname}-%{version}
# Requires sphinx>=8.0.2, sphinx in Fedora lacks 6 months behind at the moment
sed -i -e "s/sphinx>=[0-9.]*/sphinx/g" pyproject.toml
# Relax the version constraint of hatchling, it is unnecessarily strict for EL10
sed -i -e "s/hatchling>=1.27/hatchling>=1.24/" pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files %{altname}

# %%check
# %%pytest

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
