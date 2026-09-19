%global source0_hash none

Name:           python-graphviz
Version:        0.21
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Simple Python interface for Graphviz

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/xflr6/graphviz
Source:         %{pypi_source graphviz}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'graphviz' generated automatically by pyp2spec.}

Patch0:         python-graphviz-deps.patch

%description %_description

%package -n     python3-graphviz
Summary:        %{summary}

%description -n python3-graphviz %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-graphviz dev,docs,test


%prep
%autosetup -p1 -n graphviz-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-graphviz -f %{pyproject_files}

%changelog
%autochangelog
