%global source0_hash e76160286bbfb0821602c6c0c3220ebcf366ad3246d3b9d0a0fbefcd35e86043
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libsemanage
Version: 3.11
Release: 1%{?dist}
Summary: SELinux policy management library
License: LGPL-2.1-or-later
URL: https://github.com/SELinuxProject/selinux
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsemanage-%{version}.tar.gz
Source1: libsemanage-%{version}.tar.gz.asc
Source2: semanage-key.gpg
Source3: semanage.conf

Requires: libselinux%{?_isa} >= 3.11
Requires: bzip2
Requires: audit%{?_isa} >= 4.2.1

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: make
BuildRequires: libselinux-devel >= 3.11
BuildRequires: libsepol-devel >= 3.11
BuildRequires: audit-devel >= 4.2.1
BuildRequires: bzip2-devel

%description
libsemanage manages the active SELinux policy.

%package devel
Summary: Development files for libsemanage
Requires: libsemanage%{?_isa} = %{version}-%{release}
Requires: libselinux-devel%{?_isa} >= 3.11

%description devel
Headers and the libsemanage link library.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n libsemanage-%{version} -p1

%build
%oreon_make LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} all

%install
%oreon_make_install LIBDIR=%{_libdir} SHLIBDIR=%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/selinux
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/selinux/semanage.conf
rm -f %{buildroot}%{_libdir}/*.a
%oreon_filelist_devel
sed -i '\|%{_sysconfdir}/selinux/semanage.conf|d' %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license LICENSE
%dir %{_sysconfdir}/selinux
%config(noreplace) %{_sysconfdir}/selinux/semanage.conf

%files devel -f %{_builddir}/%{name}-devel.files
