%global source0_hash none

Name:           python-repoze-who-plugins-sa
Version:        1.0~b3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The repoze.who SQLAlchemy plugin

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://code.gustavonarea.net/repoze.who.plugins.sa/
Source:         %{pypi_source repoze.who.plugins.sa-1.0b3-r3125 1.0b3.post3125}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'repoze-who-plugins-sa' generated automatically by pyp2spec.}

Patch101: repoze-who-plugins-sa-requires.patch

%description %_description

%package -n     python3-repoze-who-plugins-sa
Summary:        %{summary}

%description -n python3-repoze-who-plugins-sa %_description


%prep
%autosetup -p1 -n repoze.who.plugins.sa-1.0b3-r3125-1.0b3.post3125


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


%files -n python3-repoze-who-plugins-sa -f %{pyproject_files}

%changelog
%autochangelog
