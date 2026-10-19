%global source0_hash a984e78d8e2f6d1361afe96cab83bd04ef8ab25ed71017d5e3db9e4fa0c5672a
Name:           python-google-crc32c
Version:        1.8.0
Release:        1%{?dist}
Summary:        A python wrapper of the C library ‘Google CRC32C’
License:        Apache-2.0
URL:            https://github.com/googleapis/python-crc32c
Source0:        https://github.com/googleapis/python-crc32c/archive/v%{version}/python-crc32c-%{version}.tar.gz
Patch:          %{url}/pull/325.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-crc32c = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-google-crc32c
Summary:        A python wrapper of the C library ‘Google CRC32C’
%description -n python3-google-crc32c

%prep

%autosetup -p1
# This is a git submodule, so the bundled library isn’t included in the GitHub
# source archive, but it doesn’t hurt to be very certain.
rm -rv google_crc32c/

%install
%pyproject_install
rm -v '%{buildroot}%{python3_sitearch}/google_crc32c/_crc32c.c'
sed -r -i 's@.*/_crc32c\.c$@# &@' %{pyproject_files}
%oreon_autofiles python3-google-crc32c usr/lib/python3*/site-packages/google_crc32c* usr/lib64/python3*/site-packages/google_crc32c* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_crc32c* usr/lib64/python3*/site-packages/google_crc32c* usr/bin/*

%build

%pyproject_wheel
%check

pushd scripts >/dev/null
%{py3_test_envvars} %{python3} -m check_crc32c_extension
popd >/dev/null
%pytest
%files
%files -n python3-google-crc32c -f %{oreon_filedir}/python3-google-crc32c.list

%changelog

%autochangelog
