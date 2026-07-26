%global source0_hash 103335d08567ad8468faf1425f575e3b698e9621f9323949a6c8b96d9793e80b

%global project_name sphinxext-opengraph
%global pypi_name    sphinxext_opengraph

Name:           python-%{project_name}
Version:        0.13.0
Release:        %autorelease
Summary:        Sphinx extension to generate unique OpenGraph metadata

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://%{project_name}.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/%{project_name}/%{pypi_name}-%{version}.tar.gz

# Use system Roboto font family instead of Roboto Flex
#   (Roboto Flex is not available in Fedora repo)
Patch0:         sphinxext-opengraph-0.12.0-use-roboto-fonts.patch

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       google-roboto-fonts

%global _description %{expand:
%{summary}.}

%description %_description

%package -n python3-%{project_name}
Summary:        %{summary}

%description -n python3-%{project_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
mv LICENCE.rst LICENSE.rst
%pyproject_install
%pyproject_save_files '*'

%files -n python3-%{project_name} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst

%changelog
%autochangelog
