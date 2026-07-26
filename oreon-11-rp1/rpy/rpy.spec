%global source0_hash 837e2f74583658a5c4c339761a73f9434f33ef9ced3e30c64da7562165c2801b

%global srcname rpy
%global sum Python interface to the R language
%global rmaj   4
%if (0%{?fedora} && 0%{?fedora} >= 42)
%global rmin   5
%else
%global rmin   4
%endif

%define add_rver() %{lua:
  local dep  = rpm.expand("%1")
  local rmaj = rpm.expand("%{rmaj}")
  local rmin = rpm.expand("%{rmin}")
  print(dep .. " >= " .. rmaj .. "." .. rmin .. ", ")
  print(dep .. " < " .. rmaj .. "." .. rmin + 1)
}

Name:          rpy
Version:       3.5.16
Release:       11%{?dist}
Summary:       %{sum}
License:       GPL-2.0-or-later
Url:           https://pypi.python.org/pypi/rpy2
Source:        https://files.pythonhosted.org/packages/source/r/%{srcname}2/%{srcname}2-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: gcc
BuildRequires: %add_rver R-devel
BuildRequires: python3-devel
BuildRequires: readline-devel
BuildRequires: python3dist(pytest)

Requires:      python3-%{srcname} = %{version}-%{release}

%global _description %{expand:
RPy provides a robust Python interface to the R
programming language.  It can manage all kinds of R objects and can
execute arbitrary R functions. All the errors from the R language are
converted to Python exceptions.}

%description %_description

%package -n python3-%{srcname}
Summary:       %{sum}
Requires:      %add_rver R-core

%description -n python3-%{srcname} %_description

# Pandas will drop i686
# https://bugzilla.redhat.com/show_bug.cgi?id=2263999
%ifnarch %{xi86}
%global extras all,numpy,pandas
%else
%global extras numpy
%endif
%{pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} %{extras}}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}2-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}2 '_rinterface_cffi_*'

%check
# cd %{srcname}2
%pytest

%files

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS NEWS PKG-INFO
%license gpl-2.0.txt

%changelog
%autochangelog
