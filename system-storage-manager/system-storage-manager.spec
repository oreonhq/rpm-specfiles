%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           system-storage-manager
Version:        1.3
Release:        27%{?dist}
Summary:        A single tool to manage your storage

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://system-storage-manager.github.io/
Source0:        https://github.com/system-storage-manager/ssm/archive/%{name}-%{version}.tar.gz

Patch1:         python3-sphinx.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pwquality
Requires:       util-linux
Requires:       which
Requires:       xfsprogs
Requires:       e2fsprogs
Requires:       python3-pwquality


%description
System Storage Manager provides an easy to use command line interface to manage
your storage using various technologies like lvm, btrfs, encrypted volumes and
more.

In more sophisticated enterprise storage environments, management with Device
Mapper (dm), Logical Volume Manager (LVM), or Multiple Devices (md) is becoming
increasingly more difficult.  With file systems added to the mix, the number of
tools needed to configure and manage storage has grown so large that it is
simply not user friendly.  With so many options for a system administrator to
consider, the opportunity for errors and problems is large.

The btrfs administration tools have shown us that storage management can be
simplified, and we are working to bring that ease of use to Linux file systems
in general.

You should install the ssm if you need to manage your storage with various
technologies via a single unified interface.


%prep
%setup -q -n ssm-%{name}-%{version}

# fedora-specific issue with the name of python3-sphinx binaries
%patch -P1 -p1

# there is no assert_ method in Python 3.12+
sed -i 's/assert_/assertTrue/' tests/unittests/test_ssm.py

%build
make docs


%install
rm -rf ${RPM_BUILD_ROOT}
%{__python3} setup.py install --root=${RPM_BUILD_ROOT}
if [ "%{_pkgdocdir}" != "%{_docdir}/%{name}-%{version}" ]; then
    mv ${RPM_BUILD_ROOT}/{%{_docdir}/%{name}-%{version},%{_pkgdocdir}}
fi

%check
%{__python3} test.py || :


%files
%{_bindir}/ssm
%{_pkgdocdir}/
%{_mandir}/man8/ssm.8*
%{python3_sitelib}/ssmlib/
%{python3_sitelib}/*.egg-info


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-27
- Prepare for Oreon 11 (RP1)
