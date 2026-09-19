%global source0_hash none

Name:           python-eccodes
Version:        2.48.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python interface to the ecCodes GRIB and BUFR decoder/encoder

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ecmwf/eccodes-python
Source:         %{pypi_source eccodes}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'eccodes' generated automatically by pyp2spec.}

Patch1:         python-eccodes-setup.patch
Patch2:         python-eccodes-sphinx-config.patch
Patch3:         python-eccodes-disable-findlibs.patch

%description %_description

%package -n     python3-eccodes
Summary:        %{summary}

%description -n python3-eccodes %_description


%prep
%autosetup -p1 -n eccodes-%{version}


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


%files -n python3-eccodes -f %{pyproject_files}

%changelog
%autochangelog
