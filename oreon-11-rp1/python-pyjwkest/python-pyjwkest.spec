%global source0_hash none

Name:           python-pyjwkest
Version:        1.4.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python implementation of JWT, JWE, JWS and JWK

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/IdentityPython/pyjwkest
Source:         %{pypi_source pyjwkest}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyjwkest' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyjwkest
Summary:        %{summary}

%description -n python3-pyjwkest %_description


%prep
%autosetup -p1 -n pyjwkest-%{version}


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


%files -n python3-pyjwkest -f %{pyproject_files}

%changelog
%autochangelog
