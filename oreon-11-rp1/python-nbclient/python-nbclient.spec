%global source0_hash none

Name:           python-nbclient
Version:        0.11.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A client library for executing notebooks. Formerly nbconvert_s ExecutePreprocessor.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://jupyter.org
Source:         %{pypi_source nbclient}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nbclient' generated automatically by pyp2spec.}

Patch:          https://github.com/jupyter/nbclient/commit/b42ad03acc0bb1ed26db65ab72ac617679cbbb62.patch

%description %_description

%package -n     python3-nbclient
Summary:        %{summary}

%description -n python3-nbclient %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nbclient dev,docs,test


%prep
%autosetup -p1 -n nbclient-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nbclient -f %{pyproject_files}
%{_bindir}/jupyter-execute

%changelog
%autochangelog
