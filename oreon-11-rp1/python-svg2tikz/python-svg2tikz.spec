%global source0_hash none

Name:           python-svg2tikz
Version:        3.3.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Tools for converting SVG graphics to TikZ/PGF code

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            ...
Source:         %{pypi_source svg2tikz}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'svg2tikz' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-svg2tikz
Summary:        %{summary}

%description -n python3-svg2tikz %_description


%prep
%autosetup -p1 -n svg2tikz-%{version}


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


%files -n python3-svg2tikz -f %{pyproject_files}
%{_bindir}/svg2tikz

%changelog
%autochangelog
