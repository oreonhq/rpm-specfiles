%global source0_hash none

Name:           python-mailmerge
Version:        2.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A simple, command line mail merge tool

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/awdeorio/mailmerge/
Source:         %{pypi_source mailmerge}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mailmerge' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mailmerge
Summary:        %{summary}

%description -n python3-mailmerge %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-mailmerge dev,test


%prep
%autosetup -p1 -n mailmerge-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-mailmerge -f %{pyproject_files}
%{_bindir}/mailmerge

%changelog
%autochangelog
