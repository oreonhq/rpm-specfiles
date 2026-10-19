%global source0_hash f33ff8ea9a5f3e561a781fd844f549694c119677f07a97703d4c12b49a78f6d1
%global common_description %{expand:
mujson lets python libraries make use of the most performant JSON functions
available at import time.  It is small, and does not itself implement any
encoding or decoding functionality.}
Name:           python-mujson
Version:        1.4
Release:        1%{?dist}
Summary:        Use the fastest JSON functions available at import time
License:        MIT
URL:            https://github.com/mattgiles/mujson
Source0:        https://github.com/mattgiles/mujson/archive/%{version}/mujson-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mujson = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-mujson
Summary:        Use the fastest JSON functions available at import time
BuildRequires:  python3-devel
%description -n python3-mujson %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mujson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mujson usr/lib/python3*/site-packages/mujson* usr/lib64/python3*/site-packages/mujson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mujson* usr/lib64/python3*/site-packages/mujson* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-mujson -f %{oreon_filedir}/python3-mujson.list

%changelog

%autochangelog
