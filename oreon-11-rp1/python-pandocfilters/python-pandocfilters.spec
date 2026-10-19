%global source0_hash 002b4a555ee4ebc03f8b66307e287fa492e4a77b4ea14d3f934328297bb4939e
Name:		python-pandocfilters
Version:	1.5.1
Release:        1%{?dist}
Summary:        Python module for writing pandoc filters
License:	BSD-3-Clause
URL:		https://github.com/jgm/pandocfilters
Source0:        https://files.pythonhosted.org/packages/source/p/pandocfilters/pandocfilters-%{version}.tar.gz
BuildArch:	noarch
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pandocfilters = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pandocfilters
Summary:	Python module for writing pandoc filters
%{?python_provide:%python_provide python3-pandocfilters}
%description -n python3-pandocfilters

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pandocfilters-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pandocfilters usr/lib/python3*/site-packages/pandocfilters* usr/lib64/python3*/site-packages/pandocfilters* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pandocfilters* usr/lib64/python3*/site-packages/pandocfilters* usr/bin/*

%files
%files -n python3-pandocfilters -f %{oreon_filedir}/python3-pandocfilters.list

%changelog

%autochangelog
