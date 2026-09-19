%global source0_hash none

Name:           python-b4
Version:        0.16.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A tool to work with public-inbox and patch archives

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/b4/b4.git/
Source:         %{pypi_source b4}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'b4' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-b4
Summary:        %{summary}

%description -n python3-b4 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-b4 completion,tui


%prep
%autosetup -p1 -n b4-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x completion,tui


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-b4 -f %{pyproject_files}
%{_bindir}/b4

%changelog
%autochangelog
