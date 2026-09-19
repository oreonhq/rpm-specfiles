%global source0_hash f1c7c49762695cdf02c0322bbc5caff36e7fe21bf69ecb1c562ed7e7e11cf4ee

%global	module	tkrzw

Name:		python-%{module}
Version:	0.1.32
Release:	8%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
Summary:	TKRZW Python bindings
URL:		https://dbmx.net/tkrzw/
Source0:	https://dbmx.net/tkrzw/pkg-python/%{module}-python-%{version}.tar.gz
# https://github.com/estraier/tkrzw-python/issues/6
Patch0:		%{name}-%{version}.patch
BuildRequires:	gcc-c++
BuildRequires:	python3-setuptools
# python3-devel
BuildRequires:	pkgconfig(python3)
# python3-pip
BuildRequires:	python3dist(pip)
# python3-sphinx
BuildRequires:	python3dist(sphinx)
# tkrzw due tkrzw_build_util
BuildRequires:	tkrzw >= 1.0.30
# tkrzw-devel
BuildRequires:	pkgconfig(tkrzw) >= 1.0.30
# xz-devel
BuildRequires:	pkgconfig(liblzma)
# lz4-devel
BuildRequires:	pkgconfig(liblz4)
# libzstd-devel
BuildRequires:	pkgconfig(libzstd)
# zlib-devel
BuildRequires:	pkgconfig(zlib)
# Temporary disabled: https://github.com/estraier/tkrzw-python/issues/4
ExcludeArch:	i686

%description
TKRZW is a library of routines for managing a key-value database.

%package -n	python3-%{module}
Summary:	%{summary}
%if 0%{?epel} && 0%{?epel} < 9
%{?python_provide:%python_provide python3-%{module}}
%endif

%description -n	python3-%{module}
TKRZW is a library of routines for managing a key-value database.

%package	doc
Summary:	%{summary} - API documentation
BuildArch:	noarch

%description	doc
TKRZW is a library of routines for managing a key-value database.
This package contains API documentation of it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{module}-python-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%make_build apidoc

%install
%pyproject_install
%pyproject_save_files %{module}

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%make_build check

%files -n python3-%{module} -f %{pyproject_files}
%license COPYING

%files doc
%license COPYING
%doc README CONTRIBUTING.md example?.py api-doc/

%changelog
%autochangelog
