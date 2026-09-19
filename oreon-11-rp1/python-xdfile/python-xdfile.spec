%global source0_hash none

Name:           python-xd
Version:        0.1.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        a list of useful commands which makes life easier

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/damnever/xd
Source:         %{pypi_source xd}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xd' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xd
Summary:        %{summary}

%description -n python3-xd %_description


%prep
%autosetup -p1 -n xd-%{version}


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


%files -n python3-xd -f %{pyproject_files}
%{_bindir}/xd

%changelog
%autochangelog
