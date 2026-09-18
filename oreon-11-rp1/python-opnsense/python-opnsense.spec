%global source0_hash none

Name:           python-pyopnsense
Version:        0.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A python API client for OPNsense

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            ...
Source:         %{pypi_source pyopnsense}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyopnsense' generated automatically by pyp2spec.}

Patch0:         python-opnsense-rm-python-mock-usage.diff

%description %_description

%package -n     python3-pyopnsense
Summary:        %{summary}

%description -n python3-pyopnsense %_description


%prep
%autosetup -p1 -n pyopnsense-%{version}


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


%files -n python3-pyopnsense -f %{pyproject_files}

%changelog
%autochangelog
