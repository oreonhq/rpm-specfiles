%global source0_hash none

Name:           python-send2trash
Version:        2.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Send file to trash natively under Mac OS X, Windows and Linux

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/arsenetar/send2trash
Source:         %{pypi_source send2trash}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'send2trash' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-send2trash
Summary:        %{summary}

%description -n python3-send2trash %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-send2trash nativelib,test


%prep
%autosetup -p1 -n send2trash-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x nativelib,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-send2trash -f %{pyproject_files}
%{_bindir}/send2trash

%changelog
%autochangelog
