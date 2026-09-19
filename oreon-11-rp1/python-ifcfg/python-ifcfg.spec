%global source0_hash none

Name:           python-ifcfg
Version:        0.24
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python ifconfig wrapper for Unix/Linux/MacOSX + ipconfig for Windows

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ftao/python-ifcfg
Source:         %{pypi_source ifcfg}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ifcfg' generated automatically by pyp2spec.}

Patch0:         %{name}-0.21-drop-nose.patch
Patch1:         %{name}-rm-python-mock-usage.patch

%description %_description

%package -n     python3-ifcfg
Summary:        %{summary}

%description -n python3-ifcfg %_description


%prep
%autosetup -p1 -n ifcfg-%{version}


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


%files -n python3-ifcfg -f %{pyproject_files}

%changelog
%autochangelog
