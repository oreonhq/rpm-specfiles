%global source0_hash none

Name:           python-sphinxcontrib-svg2pdfconverter
Version:        2.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx SVG to PDF or PNG converter extension

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter
Source:         %{pypi_source sphinxcontrib_svg2pdfconverter}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinxcontrib-svg2pdfconverter' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinxcontrib-svg2pdfconverter
Summary:        %{summary}

%description -n python3-sphinxcontrib-svg2pdfconverter %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinxcontrib-svg2pdfconverter cairosvg


%prep
%autosetup -p1 -n sphinxcontrib_svg2pdfconverter-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cairosvg


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sphinxcontrib-svg2pdfconverter -f %{pyproject_files}

%changelog
%autochangelog
