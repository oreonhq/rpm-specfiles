%global source0_hash none

Name:           python-boltons
Version:        26.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        When they_re not builtins, they_re boltons.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/mahmoud/boltons
Source:         %{pypi_source boltons}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'boltons' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-boltons
Summary:        %{summary}

%description -n python3-boltons %_description


%prep
%autosetup -p1 -n boltons-%{version}


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


%files -n python3-boltons -f %{pyproject_files}

%changelog
%autochangelog
