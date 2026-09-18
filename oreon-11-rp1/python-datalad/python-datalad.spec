%global source0_hash none

Name:           python-datalad
Version:        1.6.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Distributed system for joint management of code, data, and their relationship

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://www.datalad.org
Source:         %{pypi_source datalad}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'datalad' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-datalad
Summary:        %{summary}

%description -n python3-datalad %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-datalad devel,devel-docs,devel-utils,downloaders-extra,duecredit,full,misc,tests


%prep
%autosetup -p1 -n datalad-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x devel,devel-docs,devel-utils,downloaders-extra,duecredit,full,misc,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-datalad -f %{pyproject_files}
%{_bindir}/datalad
%{_bindir}/git-annex-remote-datalad
%{_bindir}/git-annex-remote-datalad-archives
%{_bindir}/git-annex-remote-ora
%{_bindir}/git-annex-remote-ria
%{_bindir}/git-credential-datalad

%changelog
%autochangelog
