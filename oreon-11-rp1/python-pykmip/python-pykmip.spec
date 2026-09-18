%global source0_hash none

Name:           python-pykmip
Version:        0.11.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        KMIP library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/OpenKMIP/PyKMIP
Source:         %{pypi_source pykmip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pykmip' generated automatically by pyp2spec.}

Patch0:         enum34.patch

%description %_description

%package -n     python3-pykmip
Summary:        %{summary}

%description -n python3-pykmip %_description


%prep
%autosetup -p1 -n pykmip-%{version}


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


%files -n python3-pykmip -f %{pyproject_files}
%{_bindir}/pykmip-server

%changelog
%autochangelog
