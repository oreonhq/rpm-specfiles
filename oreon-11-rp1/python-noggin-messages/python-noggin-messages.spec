%global source0_hash none

Name:           python-noggin-messages
Version:        1.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Fedora Messaging message schemas for Noggin.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/fedora-infra/noggin-messages
Source:         %{pypi_source noggin_messages}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'noggin-messages' generated automatically by pyp2spec.}

Patch1001:      0001-Revert-Include-additional-files-in-the-sdist.patch

%description %_description

%package -n     python3-noggin-messages
Summary:        %{summary}

%description -n python3-noggin-messages %_description


%prep
%autosetup -p1 -n noggin_messages-%{version}


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


%files -n python3-noggin-messages -f %{pyproject_files}

%changelog
%autochangelog
