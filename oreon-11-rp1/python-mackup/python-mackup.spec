%global source0_hash none

Name:           python-mackup
Version:        0.11.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Backup and keep your application settings in sync.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0-or-later
URL:            https://github.com/lra/mackup.git
Source:         %{pypi_source mackup}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mackup' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mackup
Summary:        %{summary}

%description -n python3-mackup %_description


%prep
%autosetup -p1 -n mackup-%{version}


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


%files -n python3-mackup -f %{pyproject_files}
%{_bindir}/mackup

%changelog
%autochangelog
