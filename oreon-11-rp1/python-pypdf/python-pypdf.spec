%global source0_hash none

Name:           python-pypdf
Version:        6.19.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/py-pdf/pypdf
Source:         %{pypi_source pypdf}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pypdf' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pypdf
Summary:        %{summary}

%description -n python3-pypdf %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pypdf crypto,cryptodome,dev,docs,fonts,full,image,rtl-text


%prep
%autosetup -p1 -n pypdf-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crypto,cryptodome,dev,docs,fonts,full,image,rtl-text


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pypdf -f %{pyproject_files}

%changelog
%autochangelog
