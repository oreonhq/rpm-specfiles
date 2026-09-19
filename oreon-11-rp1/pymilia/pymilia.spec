%global source0_hash cc74292cac705f4157715b048be9a08a883e65169d25f17cfc20db539a79e606

Name: pymilia
Version: 1.0.0
Release: 52%{?dist}
Summary: Python wrappers for milia
License: GPL-3.0-or-later

URL: http://guaix.fis.ucm.es/projects/pymilia/wiki
Source0: ftp://astrax.fis.ucm.es/pub/software/pymilia/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: milia-devel >= 1.0.0

%global _description\
Python wrappers for milia. Milia is a C++ library created to\
compute cosmological distances and ages in the\
Friedmann-Lemaître-Robertson-Walker metric.

%description %_description

%package -n python3-pymilia
Summary: Python wrappers for milia
BuildRequires: python3-devel 
BuildRequires: %{py3_dist Cython}

%description -n python3-pymilia 
Python wrappers for milia. Milia is a C++ library created to 
compute cosmological distances and ages in the 
Friedmann-Lemaître-Robertson-Walker metric.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files milia

%files -n python3-pymilia -f %{pyproject_files}
%doc README.txt 

%changelog
%autochangelog
