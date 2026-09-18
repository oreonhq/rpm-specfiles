%global source0_hash none

Name:           python-fastavro
Version:        1.12.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Fast read/write of AVRO files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/fastavro/fastavro
Source:         %{pypi_source fastavro}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fastavro' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fastavro
Summary:        %{summary}

%description -n python3-fastavro %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fastavro codecs,lz4,snappy,zstandard


%prep
%autosetup -p1 -n fastavro-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x codecs,lz4,snappy,zstandard


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fastavro -f %{pyproject_files}
%{_bindir}/fastavro

%changelog
%autochangelog
