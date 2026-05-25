Name: ksmtuned
Version: 0.1.0
Release: 18%{?dist}

Summary: Kernel Samepage Merging services
License: GPL-2.0-or-later
URL: https://github.com/ksmtuned/ksmtuned
Source0: https://github.com/ksmtuned/ksmtuned/archive/v%{version}/ksmtuned-%{version}.tar.gz

# Package was originally 'ksm' as a subpackage of 'qemu'
Obsoletes: ksm < 3.0.0-0.2

BuildRequires: gcc
BuildRequires: meson
%{?systemd_requires}
BuildRequires: systemd


%description
Kernel Samepage Merging (KSM) is a memory-saving de-duplication feature,
that merges anonymous (private) pages (not pagecache ones).

This package provides service files for disabling (ksm) and tuning
(ksmtuned)


%prep
%autosetup -p1


%build
%meson \
    -Dredhat-sysconfig=true
%meson_build


%install
%meson_install


%post
%systemd_post ksm.service
%systemd_post ksmtuned.service
%preun
%systemd_preun ksm.service
%systemd_preun ksmtuned.service
%postun
%systemd_postun_with_restart ksm.service
%systemd_postun_with_restart ksmtuned.service


%files
%license COPYING
%{_libexecdir}/ksmctl
%{_sbindir}/ksmtuned
%{_unitdir}/ksmtuned.service
%{_unitdir}/ksm.service
%config(noreplace) %{_sysconfdir}/ksmtuned.conf
%config(noreplace) %{_sysconfdir}/sysconfig/ksm


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.0-18
- Import
