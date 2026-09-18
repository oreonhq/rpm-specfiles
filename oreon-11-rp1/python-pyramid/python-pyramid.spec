%global source0_hash none

Name:           python-pyramid
Version:        2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The Pyramid Web Framework, a Pylons project

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LicenseRef-Repoze-BSD-derived
URL:            https://trypyramid.com
Source:         %{pypi_source pyramid}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyramid' generated automatically by pyp2spec.}

Patch:          https://github.com/Pylons/pyramid/pull/3762.patch

%description %_description

%package -n     python3-pyramid
Summary:        %{summary}

%description -n python3-pyramid %_description


%prep
%autosetup -p1 -n pyramid-%{version}


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


%files -n python3-pyramid -f %{pyproject_files}
%{_bindir}/pdistreport
%{_bindir}/prequest
%{_bindir}/proutes
%{_bindir}/pserve
%{_bindir}/pshell
%{_bindir}/ptweens
%{_bindir}/pviews

%changelog
%autochangelog
