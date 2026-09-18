%global source0_hash none

Name:           python-beniget
Version:        0.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Extract semantic information about static Python code

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/serge-sans-paille/beniget/
Source:         %{pypi_source beniget}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'beniget' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-beniget
Summary:        %{summary}

%description -n python3-beniget %_description


%prep
%autosetup -p1 -n beniget-%{version}


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


%files -n python3-beniget -f %{pyproject_files}

%changelog
%autochangelog
