%global source0_hash none

Name:           python-argcomplete
Version:        3.7.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Bash tab completion for argparse

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/kislyuk/argcomplete
Source:         %{pypi_source argcomplete}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'argcomplete' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-argcomplete
Summary:        %{summary}

%description -n python3-argcomplete %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-argcomplete test


%prep
%autosetup -p1 -n argcomplete-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-argcomplete -f %{pyproject_files}
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/register-python-argcomplete

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.3-1
- Import
