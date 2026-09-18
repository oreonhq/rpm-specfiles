%global source0_hash none

Name:           python-blobfile
Version:        3.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Read GCS, ABS and local paths with the same interface, clone of tensorflow.io.gfile

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/blobfile/blobfile
Source:         %{pypi_source blobfile}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blobfile' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-blobfile
Summary:        %{summary}

%description -n python3-blobfile %_description


%prep
%autosetup -p1 -n blobfile-%{version}


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


%files -n python3-blobfile -f %{pyproject_files}

%changelog
%autochangelog
