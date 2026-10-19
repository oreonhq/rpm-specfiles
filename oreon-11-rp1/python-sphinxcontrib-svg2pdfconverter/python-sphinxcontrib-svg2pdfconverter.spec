%global source0_hash 9756e82d5f3bf11629ffcbafb1f8a1092d3bb4789e33494032cdce9a9c8459d3
Name:           python-sphinxcontrib-svg2pdfconverter
Version:        2.1.0
Release:        1%{?dist}
Summary:        Sphinx SVG to PDF or PNG converter extension
License:        BSD-2-Clause
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_svg2pdfconverter/sphinxcontrib_svg2pdfconverter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-sphinxcontrib-svg2pdfconverter = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxcontrib-svg2pdfconverter+CairoSVG
Summary:        Metapackage for python3-sphinxcontrib-svg2pdfconverter CairoSVG extras
Requires:       python3-sphinxcontrib-svg2pdfconverter = %{version}-%{release}
Requires:       python3dist(cairosvg) >= 1.0
Provides:       python3dist(sphinxcontrib-svg2pdfconverter[CairoSVG]) = %{version}-%{release}

%description -n python3-sphinxcontrib-svg2pdfconverter+CairoSVG
Metapackage for python3-sphinxcontrib-svg2pdfconverter CairoSVG extras.

%description

%package -n     python3-sphinxcontrib-svg2pdfconverter
Summary:        Sphinx SVG to PDF or PNG converter extension
# oreon:reqs
Requires:       python3dist(sphinx) >= 1.6.3
# /oreon:reqs
%description -n python3-sphinxcontrib-svg2pdfconverter

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinxcontrib_svg2pdfconverter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-svg2pdfconverter usr/lib/python3*/site-packages/sphinxcontrib_svg2pdfconverter* usr/lib64/python3*/site-packages/sphinxcontrib_svg2pdfconverter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_svg2pdfconverter* usr/lib64/python3*/site-packages/sphinxcontrib_svg2pdfconverter* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinxcontrib-svg2pdfconverter -f %{oreon_filedir}/python3-sphinxcontrib-svg2pdfconverter.list

%changelog

%autochangelog
