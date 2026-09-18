%global source0_hash none

Name:           python-pdf2image
Version:        1.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A wrapper around the pdftoppm and pdftocairo command line tools to convert PDF to a PIL Image list.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Belval/pdf2image
Source:         %{pypi_source pdf2image}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pdf2image' generated automatically by pyp2spec.}

Patch:          %{url}/pull/269.patch

%description %_description

%package -n     python3-pdf2image
Summary:        %{summary}

%description -n python3-pdf2image %_description


%prep
%autosetup -p1 -n pdf2image-%{version}


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


%files -n python3-pdf2image -f %{pyproject_files}

%changelog
%autochangelog
