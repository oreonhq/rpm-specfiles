%global source0_hash da6341e6cde9dfcb2655b1c14a046330e30b590dca4c0e6f21cd236f20a58048
Name: python-ovirt-engine-sdk4
Summary:        Python SDK for version 4 of the oVirt Engine API
Version: 4.6.2
%global major_version %(v=%{version}; echo ${v:0:3})
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/oVirt/python-ovirt-engine-sdk4
Source0:        https://github.com/oVirt/python-ovirt-engine-sdk4/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ovirt-engine-sdk4 = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-ovirt-engine-sdk4
Summary: %summary
%description -n python3-ovirt-engine-sdk4

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
%py3_shebang_fix examples
find examples -type f -print0 | xargs -0 chmod 0644
GENERATED_FILES="
 lib/ovirtsdk4/version.py
 setup.py
 PKG-INFO
 lib/ovirt_engine_sdk_python.egg-info/PKG-INFO
 python-ovirt-engine-sdk4.spec
"

for gen_file in ${GENERATED_FILES} ; do
  sed \
    -e "s|@RPM_VERSION@|%{version}|g" \
    -e "s|@RPM_RELEASE@|%{release}|g" \
    -e "s|@PACKAGE_NAME@|%{name}|g" \
    -e "s|@PACKAGE_VERSION@|%{package_version}|g" \
    < ${gen_file}.in > ${gen_file}
done

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ovirt-engine-sdk4 usr/lib/python3*/site-packages/ovirt_engine_sdk4* usr/lib64/python3*/site-packages/ovirt_engine_sdk4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ovirt_engine_sdk4* usr/lib64/python3*/site-packages/ovirt_engine_sdk4* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-ovirt-engine-sdk4 -f %{oreon_filedir}/python3-ovirt-engine-sdk4.list

%changelog

%autochangelog
