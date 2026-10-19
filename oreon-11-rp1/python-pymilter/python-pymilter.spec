%global source0_hash 1c30abcf4b229e0e0f526a4e61eb7a7e9d88e14c6101001353b8219719325fcb
Name:           python-pymilter
Version:        1.0.6
Release:        1%{?dist}
Summary:        Python interface to sendmail milter API
Group:          Development/Libraries
License:        GPL-2.0-or-later
URL:            https://www.pymilter.org
Source0:        https://github.com/sdgathman/pymilter/archive/pymilter-%{version}.tar.gz
Source1:        tmpfiles-python-pymilter.conf
Patch0:         pymilter-check.patch
Patch1:         https://github.com/sdgathman/pymilter/pull/65.patch
Patch2:         https://github.com/sdgathman/pymilter/pull/70.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pymilter = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pymilter
Summary:        Python interface to sendmail milter API
Requires:       python3-py3dns
Requires:       %{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-pymilter}
%description -n python3-pymilter

%package common
Summary:        Common files and directories for python milters
BuildArch:      noarch
%description common
Common files and directories used for python milters

%package selinux
Summary:        SELinux policy module for pymilter
Group:          System Environment/Base
Requires:       policycoreutils, selinux-policy-targeted
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  checkpolicy
BuildRequires:  policycoreutils
BuildRequires:  policycoreutils-python-utils
BuildRequires:  selinux-policy-devel
%description selinux
Give sendmail_t additional access to stream sockets used to communicate
with milters.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pymilter-pymilter-%{version}
#setup -q -n pymilter-%%{version}
%patch -P0 -p1 -b .check
%patch -P1 -p1 -b .check
%patch -P2 -p1 -b .check
cp -p template.py milter-template.py

# Fix version
# setup.py has not been updated in tag 1.0.6
# https://github.com/sdgathman/pymilter/blob/pymilter-1.0.6/setup.py
sed -r -i 's/1\.0\.5/%{version}/' setup.py

# Fix policy test
# https://github.com/sdgathman/pymilter/issues/62
sed -r -i 's/(access_file_nulls) *= *True/\1 = False/g' testpolicy.py

%build

%pyproject_wheel
checkmodule -m -M -o pymilter.mod pymilter.te
semodule_package -o pymilter.pp -m pymilter.mod
%install
%pyproject_install
mkdir -p %{buildroot}/run/milter
mkdir -p %{buildroot}%{_localstatedir}/log/milter
mkdir -p %{buildroot}%{_libexecdir}/milter
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
mkdir -p %{buildroot}%{_datadir}/selinux/targeted
cp -p pymilter.pp %{buildroot}%{_datadir}/selinux/targeted
%oreon_autofiles python3-pymilter usr/lib/python3*/site-packages/pymilter* usr/lib64/python3*/site-packages/pymilter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymilter* usr/lib64/python3*/site-packages/pymilter* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_test_envvars %python3 test.py
%post selinux

%{_sbindir}/semodule -s targeted -i %{_datadir}/selinux/targeted/pymilter.pp \
        &>/dev/null || :
%postun selinux

if [ $1 -eq 0 ] ; then
%{_sbindir}/semodule -s targeted -r pymilter &> /dev/null || :
fi
%files
%files -n python3-pymilter -f %{oreon_filedir}/python3-pymilter.list
%files -n python-pymilter-common -f %{oreon_filedir}/python-pymilter-common.list
%files -n python-pymilter-selinux -f %{oreon_filedir}/python-pymilter-selinux.list

%changelog

%autochangelog
