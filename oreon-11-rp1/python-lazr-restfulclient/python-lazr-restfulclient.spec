%global source0_hash none

Name:           python-lazr-restfulclient
Version:        4.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A programmable client library that takes advantage of the commonalities among lazr.restful web services.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://launchpad.net/lazr.restfulclient
Source:         %{pypi_source lazr_restfulclient}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lazr-restfulclient' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-lazr-restfulclient
Summary:        %{summary}

%description -n python3-lazr-restfulclient %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-lazr-restfulclient docs,test


%prep
%autosetup -p1 -n lazr_restfulclient-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-lazr-restfulclient -f %{pyproject_files}

%changelog
%autochangelog
