%global source0_hash none

Name:           python-pysam
Version:        0.24.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Package for reading, manipulating, and writing genomic data

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://pysam.readthedocs.io/
Source:         %{pypi_source pysam}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pysam' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pysam
Summary:        %{summary}

%description -n python3-pysam %_description


%prep
%autosetup -p1 -n pysam-%{version}


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


%files -n python3-pysam -f %{pyproject_files}

%changelog
%autochangelog
