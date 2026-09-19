%global source0_hash none

Name:           python-rich-click
Version:        1.9.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Format click help output nicely with rich

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ewels/rich-click
Source:         %{pypi_source rich_click}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rich-click' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-rich-click
Summary:        %{summary}

%description -n python3-rich-click %_description


%prep
%autosetup -p1 -n rich_click-%{version}


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


%files -n python3-rich-click -f %{pyproject_files}
%{_bindir}/rich-click

%changelog
%autochangelog
