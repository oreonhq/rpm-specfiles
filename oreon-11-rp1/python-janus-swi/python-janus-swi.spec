%global source0_hash 5eb78286220564f5a318e4faaabf83ef7055bc8a3ec6971ace5c51ef8bd6b09a
%global giturl  https://github.com/SWI-Prolog/packages-swipy
Name:           python-janus-swi
Version:        1.5.2
Release:        1%{?dist}
Summary:        Bidirectional interface between SWI Prolog and Python
License:        BSD-2-Clause
URL:            https://www.swi-prolog.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/janus-%{version}.tar.gz
ExcludeArch:    %{ix86}
%global common_desc %{expand:This package implements a ready-to-use bidirectional interface between SWI
Prolog and Python.}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  python3dist(pytest)
BuildRequires:  swi-prolog-core-packages
# /oreon:deps
%description
%common_desc

%package -n python3-janus-swi
Summary:        Bidirectional interface between SWI Prolog and Python
Requires:       swi-prolog-core-packages
%description -n python3-janus-swi
%common_desc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n packages-swipy-janus-%{version}

%conf
# Avoid unwanted rpaths
sed -i 's|-rpath={props\["PLLIBDIR"\]},||' setup.py

%build -p

export LDSHARED="gcc -shared"
%install
%pyproject_install
%oreon_autofiles python3-janus-swi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-janus-swi -f %{oreon_filedir}/python3-janus-swi.list

%changelog

%autochangelog
