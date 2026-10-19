%global source0_hash 19006c799fa0f5e198bc1371d551e672b03c799d67dea61d0670edc88e0df971
%global srcname dbus-client-gen
Name:           python-%{srcname}
Version:        0.5.2
Release:        1%{?dist}
Summary:        Library for Generating D-Bus Client Code
License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-client-gen
Source0:        https://github.com/stratis-storage/dbus-client-gen/archive/refs/tags/v%{version}.tar.gz#/dbus-client-gen-0.5.2.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-dbus-client-gen = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Library for Generating D-Bus Client Code
BuildRequires:  python3-devel
%description -n python3-%{srcname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/dbus_client_gen* usr/lib64/python3*/site-packages/dbus_client_gen* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-dbus-client-gen -f %{oreon_filedir}/python3-dbus-client-gen.list

%changelog

%autochangelog
