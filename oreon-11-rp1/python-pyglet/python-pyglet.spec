%global source0_hash none

Name:           python-pyglet
Version:        2.1.16
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        pyglet is a cross-platform games and multimedia package.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://pyglet.org
Source:         %{pypi_source pyglet}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyglet' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyglet
Summary:        %{summary}

%description -n python3-pyglet %_description


%prep
%autosetup -p1 -n pyglet-%{version}


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


%files -n python3-pyglet -f %{pyproject_files}

%changelog
%autochangelog
