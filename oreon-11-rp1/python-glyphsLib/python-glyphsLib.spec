%global source0_hash none

Name:           python-glyphslib
Version:        6.14.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A bridge from Glyphs source files _.glyphs_ to UFOs

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/googlefonts/glyphsLib
Source:         %{pypi_source glyphslib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'glyphslib' generated automatically by pyp2spec.}

Patch:          %{url}/pull/1073.patch

%description %_description

%package -n     python3-glyphslib
Summary:        %{summary}

%description -n python3-glyphslib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-glyphslib colr,defcon,ufo-normalization


%prep
%autosetup -p1 -n glyphslib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x colr,defcon,ufo-normalization


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-glyphslib -f %{pyproject_files}
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs

%changelog
%autochangelog
