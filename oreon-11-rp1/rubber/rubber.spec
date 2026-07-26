%global source0_hash 47bbf8d6511f6d85f98baebbebb7cb1a58e9e6b1f92ff09fa6d8c08a683ea665

%global srcname latex-rubber

Name: rubber
Version: 1.6.1
Release: 14%{?dist}
Summary: An automated system for building LaTeX documents

License: GPL-1.0-or-later

URL: https://gitlab.com/latex-rubber/rubber
Source0: %{pypi_source}
BuildArch: noarch
BuildRequires: python3-devel 
BuildRequires: %{py3_dist setuptools}

Requires: tex(latex)

%description
This is a building system for LaTeX documents. It is based on a routine that
runs just as many compilations as necessary. The module system provides a
great flexibility that virtually allows support for any package with no user
intervention, as well as pre- and post-processing of the document. The
standard modules currently provide support for bibtex, dvips, dvipdfm, pdftex,
makeindex. A good number of standard packages are supported, including
graphics/graphicx (with automatic conversion between various formats and
Metapost compilation).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files rubber

%files -f %{pyproject_files}
%doc COPYING
%{_bindir}/rubber
%{_bindir}/rubber-info
%{_bindir}/rubber-lsmod
%{_bindir}/rubber-pipe

%changelog
%autochangelog
