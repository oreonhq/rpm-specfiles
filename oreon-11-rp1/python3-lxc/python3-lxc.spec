%global source0_hash 59c2d46106621df40eb3de331521c5664a71fe35a43ec1d640ec3a88d4e4730e

Name:           python3-lxc
Version:        5.0.0
Release:        16%{?dist}
Summary:        Python binding for LXC
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
# see https://github.com/lxc/python3-lxc/issues/35
Patch0:         lxc-5.0.0_py3.13.patch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  lxc-devel >= 3.0.0
BuildRequires:  pkgconfig
BuildRequires:  gcc

%global desc Linux Resource Containers provide process and resource isolation\
without the overhead of full virtualization.\
\
The python%{python3_pkgversion}-lxc package contains the Python3\
binding for LXC.

%description
%{desc}

%if 0%{?python3_pkgversion} != 3
%global subpkg -n python%{python3_pkgversion}-lxc
%package %{?subpkg}
Summary: Python binding for LXC

%description %{?subpkg}
%{desc}
%endif

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}_lxc\\..*\\.so

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l _lxc lxc

# fix examples
chmod -x examples/*.py
sed -i -e '1 s@^#!.*@#!%{__python3}@' examples/*.py

%check
%pyproject_check_import

%py3_check_import lxc _lxc

%files %{?subpkg} -f %{pyproject_files}
%doc README.md examples

%changelog
%autochangelog
