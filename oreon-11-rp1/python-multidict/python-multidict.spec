%global source0_hash none

Name:           python-multidict
Version:        6.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        multidict implementation

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://matrix.to/#/#aio-libs:matrix.org
Source:         %{pypi_source multidict}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'multidict' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-multidict
Summary:        %{summary}

%description -n python3-multidict %_description


%prep
%autosetup -p1 -n multidict-%{version}


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


%files -n python3-multidict -f %{pyproject_files}

%changelog
%autochangelog
