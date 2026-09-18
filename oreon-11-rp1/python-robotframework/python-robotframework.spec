%global source0_hash none

Name:           python-robotframework
Version:        7.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Generic automation framework for acceptance testing and robotic process automation _RPA_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/robotframework/robotframework
Source:         %{pypi_source robotframework}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'robotframework' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-robotframework
Summary:        %{summary}

%description -n python3-robotframework %_description


%prep
%autosetup -p1 -n robotframework-%{version}


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


%files -n python3-robotframework -f %{pyproject_files}
%{_bindir}/libdoc
%{_bindir}/rebot
%{_bindir}/robot

%changelog
%autochangelog
