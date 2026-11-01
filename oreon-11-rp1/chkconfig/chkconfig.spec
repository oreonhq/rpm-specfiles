%global source0_hash 47350674fe203fcfb51e9819d2f4262ac2f8a062fd08de0f9023c606677b3874
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: chkconfig
Version: 1.32
Release: 1%{?dist}
Summary: System services and alternatives management tool
License: GPL-2.0-only
URL: https://github.com/fedora-sysv/chkconfig
Source0: https://github.com/fedora-sysv/chkconfig/archive/%{version}/chkconfig-%{version}.tar.gz
Provides: alternatives = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: popt-devel
BuildRequires: libselinux-devel
BuildRequires: libsepol-devel
BuildRequires: gettext
BuildRequires: pkgconf
%endif

%description
chkconfig manages SysV init script links; this package also ships the
alternatives tool for maintaining symbolic links to default commands.

%prep
%oreon_sha256
%autosetup -n chkconfig-%{version} -p1

%build
make -s %{?_smp_mflags} RPM_OPT_FLAGS="%{_oreon_cflags}" LDFLAGS="%{_oreon_ldflags}" VERSION=%{version} MERGED_SBIN=1 subdirs chkconfig alternatives

%install
install -Dpm0755 chkconfig %{buildroot}%{_sbindir}/chkconfig
install -Dpm0755 alternatives %{buildroot}%{_sbindir}/alternatives
ln -s alternatives %{buildroot}%{_sbindir}/update-alternatives
install -Dpm0644 chkconfig.8 %{buildroot}%{_mandir}/man8/chkconfig.8
install -Dpm0644 alternatives.8 %{buildroot}%{_mandir}/man8/alternatives.8
ln -s alternatives.8 %{buildroot}%{_mandir}/man8/update-alternatives.8
make -s -C po install PREFIX=%{buildroot}%{_prefix} DESTDIR=%{buildroot} || :
mkdir -p %{buildroot}%{_sysconfdir}/alternatives %{buildroot}%{_localstatedir}/lib/alternatives
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
%dir %{_sysconfdir}/alternatives
%dir %{_localstatedir}/lib/alternatives
