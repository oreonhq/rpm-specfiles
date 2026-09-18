%global source0_hash none

Name:           python-cerealizer
Version:        0.8.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A secure pickle-like module

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0
URL:            http://www.lesfleursdunormal.fr/static/informatique/cerealizer/index_en.html
Source:         %{pypi_source Cerealizer}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cerealizer' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cerealizer
Summary:        %{summary}

%description -n python3-cerealizer %_description


%prep
%autosetup -p1 -n Cerealizer-%{version}


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


%files -n python3-cerealizer -f %{pyproject_files}

%changelog
%autochangelog
