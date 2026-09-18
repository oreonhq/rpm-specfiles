%global source0_hash none

Name:           python-cloud-sptheme
Version:        1.10.1^post20200504175005
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        a nice sphinx theme named _Cloud_, and some related extensions

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://cloud-sptheme.readthedocs.io
Source:         %{pypi_source cloud_sptheme 1.10.1.post20200504175005}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cloud-sptheme' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cloud-sptheme
Summary:        %{summary}

%description -n python3-cloud-sptheme %_description


%prep
%autosetup -p1 -n cloud_sptheme-1.10.1.post20200504175005


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-cloud-sptheme -f %{pyproject_files}

%changelog
%autochangelog
