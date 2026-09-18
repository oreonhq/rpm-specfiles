%global source0_hash none

Name:           python-repoze-tm2
Version:        2.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Per-request transactions via WSGI middleware

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LicenseRef-Repoze-BSD-derived
URL:            https://github.com/repoze/repoze.tm2
Source:         %{pypi_source repoze_tm2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'repoze-tm2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-repoze-tm2
Summary:        %{summary}

%description -n python3-repoze-tm2 %_description


%prep
%autosetup -p1 -n repoze_tm2-%{version}


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


%files -n python3-repoze-tm2 -f %{pyproject_files}

%changelog
%autochangelog
