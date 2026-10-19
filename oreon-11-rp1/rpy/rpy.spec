%global source0_hash f1fb4649ce7d14e935133088dec97cda27eb37ce7cc710385f81dca556fe8c9f
%global srcname rpy
%global sum Python interface to the R language
%global rmaj   4
%global rmin   4
%define add_rver() %{lua:
  local dep  = rpm.expand("%1")
  local rmaj = rpm.expand("%{rmaj}")
  local rmin = rpm.expand("%{rmin}")
  print(dep .. " >= " .. rmaj .. "." .. rmin .. ", ")
  print(dep .. " < " .. rmaj .. "." .. rmin + 1)
}
Name:          rpy
Version:       3.6.7
Release:        1%{?dist}
Summary:        Python interface to the R language
License:       GPL-2.0-or-later
Url:           https://pypi.python.org/pypi/rpy2
Source0:        https://files.pythonhosted.org/packages/source/r/%{name}2/%{name}2-%{version}.tar.gz
ExcludeArch: %{ix86}
Requires:      python3-%{srcname} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.15.0
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-rpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-rpy+doc
Summary:        Metapackage for python3-rpy doc extras
Requires:       python3-rpy = %{version}-%{release}
Provides:       python3dist(rpy[doc]) = %{version}-%{release}

%description -n python3-rpy+doc
Metapackage for python3-rpy doc extras.

%package -n       python3-rpy+test_minimal
Summary:        Metapackage for python3-rpy test_minimal extras
Requires:       python3-rpy = %{version}-%{release}
Requires:       python3dist(pytest) >= 8
Provides:       python3dist(rpy[test_minimal]) = %{version}-%{release}

%description -n python3-rpy+test_minimal
Metapackage for python3-rpy test_minimal extras.

%package -n       python3-rpy+test
Summary:        Metapackage for python3-rpy test extras
Requires:       python3-rpy = %{version}-%{release}
Provides:       python3dist(rpy[test]) = %{version}-%{release}

%description -n python3-rpy+test
Metapackage for python3-rpy test extras.

%package -n       python3-rpy+numpy
Summary:        Metapackage for python3-rpy numpy extras
Requires:       python3-rpy = %{version}-%{release}
Provides:       python3dist(rpy[numpy]) = %{version}-%{release}

%description -n python3-rpy+numpy
Metapackage for python3-rpy numpy extras.

%package -n       python3-rpy+pandas
Summary:        Metapackage for python3-rpy pandas extras
Requires:       python3-rpy = %{version}-%{release}
Provides:       python3dist(rpy[pandas]) = %{version}-%{release}

%description -n python3-rpy+pandas
Metapackage for python3-rpy pandas extras.

%package -n       python3-rpy+types
Summary:        Metapackage for python3-rpy types extras
Requires:       python3-rpy = %{version}-%{release}
Provides:       python3dist(rpy[types]) = %{version}-%{release}

%description -n python3-rpy+types
Metapackage for python3-rpy types extras.

%package -n       python3-rpy+all
Summary:        Metapackage for python3-rpy all extras
Requires:       python3-rpy = %{version}-%{release}
Provides:       python3dist(rpy[all]) = %{version}-%{release}

%description -n python3-rpy+all
Metapackage for python3-rpy all extras.

%description

%package -n python3-%{srcname}
Summary:       %{sum}
Requires:      %add_rver R-core
%description -n python3-%{srcname}

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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/rpy* usr/lib64/python3*/site-packages/rpy* usr/bin/*

%check

%pytest
%files
%files -n python3-rpy -f %{oreon_filedir}/python3-rpy.list

%changelog

%autochangelog
