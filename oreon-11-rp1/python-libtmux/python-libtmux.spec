%global source0_hash none

Name:           python-libtmux
Version:        0.62.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Typed library that provides an ORM wrapper for tmux, a terminal multiplexer.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/tmux-python/libtmux
Source:         %{pypi_source libtmux}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'libtmux' generated automatically by pyp2spec.}

Patch:          %{srcname}-no-gp-libs.diff

%description %_description

%package -n     python3-libtmux
Summary:        %{summary}

%description -n python3-libtmux %_description


%prep
%autosetup -p1 -n libtmux-%{version}


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


%files -n python3-libtmux -f %{pyproject_files}

%changelog
%autochangelog
