%global source0_hash none

Name:           python-cbor2
Version:        6.1.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        CBOR _de_serializer with extensive tag support

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/agronholm/cbor2
Source:         %{pypi_source cbor2}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cbor2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cbor2
Summary:        %{summary}

%description -n python3-cbor2 %_description


%prep
%autosetup -p1 -n cbor2-%{version}


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


%files -n python3-cbor2 -f %{pyproject_files}
%{_bindir}/cbor2

%changelog
%autochangelog
