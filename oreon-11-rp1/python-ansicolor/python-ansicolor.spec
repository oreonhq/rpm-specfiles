%global source0_hash f66c4e3446d419813de1bfd011f6dab3d96de9369388727fed434a63e7d8edbd

%global srcname ansicolor
%global desc %{srcname} is a library to produce ANSI color output, colored highlighting\
and diffing.

%if 0%{?fedora}
  %bcond_without python3
  %if 0%{?fedora} > 29
    %bcond_with python2
  %else
    %bcond_without python2
  %endif
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

Name:           python-%{srcname}
Version:        0.2.4
Release:        37%{?dist}
Summary:        A library to produce ANSI color output

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/numerodix/%{srcname}
Source0:        https://github.com/numerodix/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
%endif
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
%endif

%description
%{desc}

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}
%endif

%package doc
Summary:        Documentation for %{name}

%description doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}

PYTHONPATH=$(pwd) ./build_docs.sh
rm -f docs/_build/html/.buildinfo

%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}

%check
%{?with_python2:py.test-%{python2_version} -v}
%{?with_python3:py.test-%{python3_version} -v}

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif

%files doc
%license LICENSE
%doc docs/_build/html/*

%changelog
%autochangelog
