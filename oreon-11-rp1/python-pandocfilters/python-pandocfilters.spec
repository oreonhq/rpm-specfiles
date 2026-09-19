%global source0_hash 002b4a555ee4ebc03f8b66307e287fa492e4a77b4ea14d3f934328297bb4939e

Name:		python-pandocfilters
Version:	1.5.1
Release:	%autorelease
Summary:	Python module for writing pandoc filters

License:	BSD-3-Clause
URL:		https://github.com/jgm/pandocfilters
Source0:	https://files.pythonhosted.org/packages/source/p/pandocfilters/pandocfilters-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel

%global _docdir_fmt %{name}

%global _description %{expand:
This package provides a few utility functions which make it easier to
write pandoc filters in Python.}

%description %_description

%package -n python3-pandocfilters
Summary:	Python module for writing pandoc filters
%{?python_provide:%python_provide python3-pandocfilters}

%description -n python3-pandocfilters %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pandocfilters-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pandocfilters

%files -n python3-pandocfilters -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
