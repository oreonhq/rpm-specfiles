%global source0_hash none

Name:           python-cogapp
Version:        3.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Cog: A content generator for executing Python snippets in source files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://cog.readthedocs.io/
Source:         %{pypi_source cogapp}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cogapp' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cogapp
Summary:        %{summary}

%description -n python3-cogapp %_description


%prep
%autosetup -p1 -n cogapp-%{version}


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


%files -n python3-cogapp -f %{pyproject_files}
%{_bindir}/cog

%changelog
%autochangelog
