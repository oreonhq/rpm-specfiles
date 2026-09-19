%global source0_hash none

Name:           python-readability
Version:        0.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Measure the readability of a given text using surface characteristics

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/andreasvc/readability/
Source:         %{pypi_source readability}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'readability' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-readability
Summary:        %{summary}

%description -n python3-readability %_description


%prep
%autosetup -p1 -n readability-%{version}


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


%files -n python3-readability -f %{pyproject_files}

%changelog
%autochangelog
