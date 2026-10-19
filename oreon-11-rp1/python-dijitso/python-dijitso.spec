%global source1_hash fbb6273ab66b8bef6c6bf28873d95ab10c59206f23eb9ab6cf5ac5c27f467747
%global source0_hash eaa45eec4457f3f865d72a926b7cba86df089410e78de04cd89b15bb405e8fd9
Name:           python-dijitso
Version:        2019.1.0
Release:        1%{?dist}
Summary:        Distributed just-in-time building of shared libraries
License:        LGPL-3.0-or-later
URL:            https://fenics-dijitso.readthedocs.org/
Source0:        https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.key
ExcludeArch: i686
%global debug_package %{nil}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dijitso = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-dijitso
Summary: %summary
%{?python_provides python3-dijitso}
Requires:       python3-mpi4py-runtime
Requires:       gcc-c++
BuildArch:      noarch
%description -n python3-dijitso

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n dijitso-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dijitso usr/lib/python3*/site-packages/dijitso* usr/lib64/python3*/site-packages/dijitso* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dijitso* usr/lib64/python3*/site-packages/dijitso* usr/bin/*

%check

%pyproject_check_import
%_mpich_load
%__python3 -m pytest -v test/
%_mpich_unload
%_openmpi_load
%__python3 -m pytest -v test/
%_openmpi_unload
%files
%files -n python3-dijitso -f %{oreon_filedir}/python3-dijitso.list

%changelog

%autochangelog
