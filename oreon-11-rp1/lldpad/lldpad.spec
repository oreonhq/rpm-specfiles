%global _default_patch_fuzz 2

# 
%global _hardened_build 1

%global checkout 85e5583

Name:               lldpad
Version:            1.1.0
Release:            16.git%{checkout}%{?dist}
Summary:            Intel LLDP Agent
License:            GPL-2.0-only
URL:                http://open-lldp.org/
Source0:            %{name}-%{version}.tar.gz

BuildRequires:      automake autoconf libtool
BuildRequires:      flex >= 2.5.33
BuildRequires:      kernel-headers >= 2.6.32
BuildRequires:      libconfig-devel >= 1.3.2
BuildRequires:      libnl3-devel
BuildRequires:      readline-devel
BuildRequires:      systemd
BuildRequires: make
Requires:           readline

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
This package contains the Linux user space daemon and configuration tool for
Intel LLDP Agent with Enhanced Ethernet support for the Data Center.

%package            devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Provides:           dcbd-devel = %{version}-%{release}
Obsoletes:          dcbd-devel < 0.9.26

%description devel
The %{name}-devel package contains header files for developing applications
that use %{name}.

%prep
%autosetup -p1

%build
./bootstrap.sh
CFLAGS=${CFLAGS:-%optflags -Wno-error -fcommon}; export CFLAGS;
%configure --disable-static
# fix the hardened build flags
sed -i -e 's! \\\$compiler_flags !&\\\$CFLAGS \\\$LDFLAGS !' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
rm -f %{buildroot}%{_libdir}/liblldp_clif.la

%post
%systemd_post %{name}.service %{name}.socket

%preun
%systemd_preun %{name}.service %{name}.socket

%postun
%systemd_postun_with_restart %{name}.service %{name}.socket

%files
%doc COPYING README ChangeLog
%{_sbindir}/*
%{_libdir}/liblldp_clif.so.*
%dir %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_sysconfdir}/bash_completion.d/*
%{_mandir}/man3/*
%{_mandir}/man8/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblldp_clif.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-16.git85e5583
- Import
