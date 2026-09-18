%global source0_hash none

Name:           python-fitsio
Version:        1.4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A full featured python library to read from and write to FITS files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/esheldon/fitsio
Source:         %{pypi_source fitsio}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fitsio' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fitsio
Summary:        %{summary}

%description -n python3-fitsio %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fitsio dev


%prep
%autosetup -p1 -n fitsio-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fitsio -f %{pyproject_files}

%changelog
%autochangelog
