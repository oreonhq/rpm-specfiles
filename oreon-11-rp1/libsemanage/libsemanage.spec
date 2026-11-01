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

Requires: libselinux%{?_isa} = 3.11-1%{?dist}
Requires: bzip2
Requires: audit%{?_isa} = 4.2.1-1%{?dist}

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
BuildRequires: libselinux-devel = 3.11-1%{?dist}
BuildRequires: libsepol-devel = 3.11-1%{?dist}
BuildRequires: audit-devel = 4.2.1-1%{?dist}
BuildRequires: bzip2-devel
BuildRequires: python3-devel
BuildRequires: swig
%endif

%description
libsemanage manages the active SELinux policy.

%package devel
Summary: Development files for libsemanage
Requires: libsemanage%{?_isa} = %{version}-%{release}
Requires: libselinux-devel%{?_isa} = 3.11-1%{?dist}

%description devel
Headers and the libsemanage link library.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n libsemanage-%{version} -p1

%build
%oreon_make swigify
%oreon_make LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} all
%oreon_make PYTHON=%{__python3} LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} pywrap

%install
%oreon_make_install LIBDIR=%{_libdir} SHLIBDIR=%{_libdir}
%oreon_make PYTHON=%{__python3} DESTDIR=%{buildroot} LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} install-pywrap
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
