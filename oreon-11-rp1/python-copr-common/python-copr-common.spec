%global source0_hash none

Name:           python-copr-common
Version:        1.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Common python code used by Copr.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/fedora-copr/copr
Source:         %{pypi_source copr_common}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'copr-common' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-copr-common
Summary:        %{summary}

%description -n python3-copr-common %_description


%prep
%autosetup -p1 -n copr_common-%{version}


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


%files -n python3-copr-common -f %{pyproject_files}

%changelog
%autochangelog
