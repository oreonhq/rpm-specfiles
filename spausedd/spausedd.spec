%bcond_without vmguestlib

Name: spausedd
Summary: Utility to detect and log scheduler pause
Version: 20210719
Release: 12%{?dist}
License: ISC
URL: https://github.com/jfriesse/spausedd
Source0: https://github.com/jfriesse/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

# VMGuestLib exists only for x86 architectures (for Fedora) and x86_64 (for RHEL)
%if %{with vmguestlib}
%if 0%{?rhel} >= 6
%ifarch x86_64
%global use_vmguestlib 1
%endif
%else
%ifarch %{ix86} x86_64
%global use_vmguestlib 1
%endif
%endif
%endif

BuildRequires: gcc
BuildRequires: make
BuildRequires: git
%{?systemd_requires}
BuildRequires: systemd

%if %{defined use_vmguestlib}
BuildRequires: pkgconfig(vmguestlib)
%endif

%description
Utility to detect and log scheduler pause

%prep
%autosetup -S git_am

%build
%set_build_flags
%make_build \
%if %{defined use_vmguestlib}
    WITH_VMGUESTLIB=1 \
%else
    WITH_VMGUESTLIB=0 \
%endif

%install
%make_install PREFIX="%{_prefix}"

mkdir -p %{buildroot}/%{_unitdir}
install -m 644 -p init/%{name}.service %{buildroot}/%{_unitdir}

%clean

%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/*
%{_unitdir}/spausedd.service

%post
%systemd_post spausedd.service

%preun
%systemd_preun spausedd.service

%postun
%systemd_postun spausedd.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20210719-12
- Prepare for Oreon 11 (RP1)
