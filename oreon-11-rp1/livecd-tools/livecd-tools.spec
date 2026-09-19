%global source0_hash 0eede6ae0a9103f3f6920587bb013a82c2045977f14801406f7b4a515c717b25

%define debug_package %{nil}

Summary:    Tools for building live CDs
Name:       livecd-tools
Version:    31.0
Release:    20%{?dist}
%if 0%{?fedora}
Epoch:      1
%endif
License:    GPL-2.0-only
URL:        https://github.com/livecd-tools/livecd-tools
# lorax dependency is not available, due to qemu removal
ExcludeArch: %{ix86}

Source0:    %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:     livecd-tools-31.0-py312-distutils-removal.patch
# Allow using local kickstart files:
Patch1:     https://github.com/livecd-tools/livecd-tools/commit/41e15de6de2caef6bfadafcaf3dbb60c0531079c.patch
# Fix mangled output with one word per line:
Patch2:     https://github.com/livecd-tools/livecd-tools/commit/51bd0fefdfd6c06c03990d46b4e7d838cefc9da4.patch

BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  python3-devel

%ifarch %{ix86} x86_64
Requires:   livecd-iso-to-mediums = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:   python3-imgcreate = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Tools for generating live CDs on Fedora based systems including derived
distributions such as RHEL, CentOS and others.
See http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%package -n python-imgcreate-sysdeps
Summary:    Common system dependencies for python-imgcreate
Requires:   coreutils
Requires:   cryptsetup
Requires:   dosfstools >= 2.11-8
Requires:   dracut
Requires:   dracut-live
Requires:   dumpet
Requires:   e2fsprogs
Requires:   isomd5sum
Requires:   lorax >= 18.3
Requires:   parted
Requires:   policycoreutils
Requires:   rsync
Requires:   selinux-policy-targeted
Requires:   squashfs-tools
Requires:   sssd-client
Requires:   util-linux
Requires:   xorriso >= 1.4.8

%if ! 0%{?rhel}
# hfs+ support for Macs
%ifarch %{ix86} x86_64 ppc ppc64
Requires:   hfsplus-tools
%endif
%endif

# syslinux dependency
%ifarch %{ix86} x86_64
Requires:   syslinux >= 6.02-4
Requires:   syslinux-nonlinux >= 6.02-4
Requires:   syslinux-extlinux
%endif

# For legacy ppc32 systems
%ifarch ppc
Requires:   yaboot
%endif

%description -n python-imgcreate-sysdeps
This package describes the common system dependencies for
python-imgcreate.

%package -n python3-imgcreate
Summary:    Python 3 modules for building system images
%{?python_provide:%python_provide python3-imgcreate}
Requires:   libselinux-python3
Requires:   python-imgcreate-sysdeps%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   python3-dbus
Requires:   python3-dnf >= 1.1.0
Requires:   python3-kickstart
Requires:   python3-pyparted
Requires:   python3-urlgrabber

%description -n python3-imgcreate
Python 3 modules that can be used for building images for things
like live image or appliances.

%ifarch %{ix86} x86_64
%package -n livecd-iso-to-mediums
Summary:    Tools for installing ISOs to different mediums
Requires:   python-imgcreate-sysdeps%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n livecd-iso-to-mediums
Tools for installing Live CD ISOs to different mediums (e.g. USB sticks, hard
drives, PXE boot, etc.)
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}

%install
%make_install PYTHON=python3

# Delete docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%ifnarch %{ix86} x86_64
# livecd-iso-to-mediums doesn't work without syslinux
rm -rfv %{buildroot}%{_bindir}/livecd-iso-to-*
rm -rfv %{buildroot}%{_mandir}/man8/livecd-iso-to-*
%endif

%files
%license COPYING
%doc AUTHORS README HACKING
%doc config/livecd-fedora-minimal.ks
%doc config/livecd-mageia-minimal-*.ks
%{_mandir}/man8/livecd-creator.8*
%{_mandir}/man8/mkbiarch.8*
%{_bindir}/livecd-creator
%{_bindir}/image-creator
%{_bindir}/liveimage-mount
%{_bindir}/editliveos
%{_bindir}/mkbiarch

%files -n python-imgcreate-sysdeps
# No files because empty metapackage

%files -n python3-imgcreate
%license COPYING
%doc API
%{python3_sitelib}/imgcreate

%ifarch %{ix86} x86_64
%files -n livecd-iso-to-mediums
%license COPYING
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_mandir}/man8/livecd-iso-to-disk.8*
%endif

%changelog
%autochangelog
