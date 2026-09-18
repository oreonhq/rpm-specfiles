%global source0_hash none

Name:           python-moddb
Version:        0.15.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A scrapper for ModDB Mod and Game pages

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ClementJ18/moddb
Source:         %{pypi_source moddb}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'moddb' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-moddb
Summary:        %{summary}

%description -n python3-moddb %_description


%prep
%autosetup -p1 -n moddb-%{version}


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


%files -n python3-moddb -f %{pyproject_files}

%changelog
%autochangelog
