%global source0_hash none

Name:           python-aw-core
Version:        0.5.18
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Core library for ActivityWatch

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://activitywatch.net/
Source:         %{pypi_source aw_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aw-core' generated automatically by pyp2spec.}

Patch:          https://github.com/ActivityWatch/aw-core/pull/127.patch

%description %_description

%package -n     python3-aw-core
Summary:        %{summary}

%description -n python3-aw-core %_description


%prep
%autosetup -p1 -n aw_core-%{version}


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


%files -n python3-aw-core -f %{pyproject_files}
%{_bindir}/aw-cli

%changelog
%autochangelog
