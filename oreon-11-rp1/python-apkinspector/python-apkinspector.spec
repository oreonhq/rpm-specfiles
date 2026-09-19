%global source0_hash none

Name:           python-apkinspector
Version:        1.3.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the AndroidManifest.xml file.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/erev0s/apkInspector
Source:         %{pypi_source apkinspector}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'apkinspector' generated automatically by pyp2spec.}

Patch:          doc.patch

%description %_description

%package -n     python3-apkinspector
Summary:        %{summary}

%description -n python3-apkinspector %_description


%prep
%autosetup -p1 -n apkinspector-%{version}


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


%files -n python3-apkinspector -f %{pyproject_files}
%{_bindir}/apkinspector

%changelog
%autochangelog
