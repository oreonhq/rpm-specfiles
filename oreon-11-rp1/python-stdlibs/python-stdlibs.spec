%global source0_hash none

Name:           python-stdlibs
Version:        2026.9.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        List of packages in the stdlib

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://stdlibs.omnilib.dev
Source:         %{pypi_source stdlibs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'stdlibs' generated automatically by pyp2spec.}

Patch:          stdlibs-use-tomllib.diff

%description %_description

%package -n     python3-stdlibs
Summary:        %{summary}

%description -n python3-stdlibs %_description


%prep
%autosetup -p1 -n stdlibs-%{version}


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


%files -n python3-stdlibs -f %{pyproject_files}

%changelog
%autochangelog
