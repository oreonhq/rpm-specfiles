%global source0_hash none

%define		baseversion 1.2.14

Summary:	Python binding for the ALSA library
Name:		python-alsa
Version:	%{baseversion}
Release:	7%{?dist}
License:	LGPL-2.1-or-later
Source0:	ftp://ftp.alsa-project.org/pub/pyalsa/pyalsa-%{version}.tar.bz2
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= %{version}
BuildRequires:	python3-devel
BuildRequires:	gcc

# Filter private shared library provides
%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\\.so$

%global _description \
Python bindings for the ALSA library.

%description %_description

%package -n python3-alsa
Summary: %summary

%description -n python3-alsa %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pyalsa-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
	
%install
%pyproject_install
%pyproject_save_files '*'

%check
%pyproject_check_import

%files -n python3-alsa -f %{pyproject_files}

%changelog
%autochangelog

