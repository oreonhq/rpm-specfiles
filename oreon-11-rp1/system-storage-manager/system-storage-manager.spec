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
# oreon url source checksums begin
%global source0_sha256 a95eb21eb0f5f0266835951c10763d0a6811f33fc717431eb9b7b18d4f564a57
%global source0_file system-storage-manager-1.3.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/system-storage-manager-1.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a95eb21eb0f5f0266835951c10763d0a6811f33fc717431eb9b7b18d4f564a57" || { echo "oreon: Source0 SHA256 mismatch for system-storage-manager-1.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-27
- Import
