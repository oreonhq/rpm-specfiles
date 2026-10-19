%global source0_hash 4603736f40648684196fb826c97704c93ca80b32ec17d066b3276a9ed1a30939
%define		baseversion 1.2.14
Summary:        Python binding for the ALSA library
Name:		python-alsa
Version:	%{baseversion}
Release:        7%{?dist}
License:	LGPL-2.1-or-later
Source0:        https://www.alsa-project.org/files/pub/pyalsa/pyalsa-%{version}.tar.bz2
URL:		http://www.alsa-project.org/
%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\\.so$
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-alsa = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-alsa
Summary: %summary
%description -n python3-alsa

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyalsa-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-alsa usr/lib/python3*/site-packages/alsa* usr/lib64/python3*/site-packages/alsa* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/alsa* usr/lib64/python3*/site-packages/alsa* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-alsa -f %{oreon_filedir}/python3-alsa.list

%changelog

%autochangelog
