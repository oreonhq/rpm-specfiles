%global source0_hash none

Name:           python-setuptools-git-versioning
Version:        3.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Use git repo data for building a version number according to PEP-440

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://setuptools-git-versioning.readthedocs.io
Source:         %{pypi_source setuptools_git_versioning}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-git-versioning' generated automatically by pyp2spec.}

Patch:      %{forgeurl}/pull/116.patch
Patch:      %{forgeurl}/pull/117.patch
Patch:      0001-Downstream-only-patch-out-coverage-analysis-machiner.patch

%description %_description

%package -n     python3-setuptools-git-versioning
Summary:        %{summary}

%description -n python3-setuptools-git-versioning %_description


%prep
%autosetup -p1 -n setuptools_git_versioning-%{version}


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


%files -n python3-setuptools-git-versioning -f %{pyproject_files}
%{_bindir}/setuptools-git-versioning

%changelog
%autochangelog
