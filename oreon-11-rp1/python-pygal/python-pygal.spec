%global source0_hash none

Name:           python-pygal
Version:        3.1.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python svg graph plotting library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-3.0-or-later
URL:            https://www.pygal.org/
Source:         %{pypi_source pygal}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pygal' generated automatically by pyp2spec.}

Patch:              https://github.com/Kozea/pygal/pull/578.patch

%description %_description

%package -n     python3-pygal
Summary:        %{summary}

%description -n python3-pygal %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pygal docs,lxml,moulinrouge,png,test


%prep
%autosetup -p1 -n pygal-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,lxml,moulinrouge,png,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pygal -f %{pyproject_files}

%changelog
%autochangelog
