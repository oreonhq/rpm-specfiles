%global source0_hash none

Name:           python-tvb-gdist
Version:        2.9.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Compute geodesic distances

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/the-virtual-brain/tvb-gdist
Source:         %{pypi_source tvb_gdist}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tvb-gdist' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tvb-gdist
Summary:        %{summary}

%description -n python3-tvb-gdist %_description


%prep
%autosetup -p1 -n tvb_gdist-%{version}


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


%files -n python3-tvb-gdist -f %{pyproject_files}

%changelog
%autochangelog
