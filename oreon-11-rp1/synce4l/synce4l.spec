%global source0_hash 200100ab77e9b5e11062e0185a6f3d898a9f1c817414df1c5d893243bafabe60

Name:		synce4l
Version:	1.1.0
Release:	6%{?dist}
Summary:	SyncE implementation for Linux

License:	GPL-2.0-or-later
URL:		https://github.com/intel/synce4l
Source0:	https://github.com/intel/synce4l/archive/%{version}/synce4l-%{version}.tar.gz
Source1:	synce4l.service

# Fix compiler warnings to avoid build failures with -Werror
Patch1:		synce4l-ccwarns.patch

BuildRequires:	gcc make systemd
BuildRequires:	libnl3-devel

%{?systemd_requires}

%description
synce4l is a software implementation of Synchronous Ethernet (SyncE) according
to ITU-T Recommendation G.8264. The design goal is to provide logic to
supported hardware by processing Ethernet Synchronization Messaging Channel
(ESMC) and control Ethernet Equipment Clock (EEC) on Network Card Interface
(NIC).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

sed \
	-e 's|^\(logging_level	*\)[0-7]|\16|' \
	-e 's|^\(use_syslog	*\)[01]|\11|' \
	-e 's|^\(verbose	*\)[01]|\10|' \
	-e 's|^\(smc_socket_path	*\)/tmp|\1/run|' \
	< configs/synce4l_dpll.cfg > synce4l.conf
touch -r configs/synce4l_dpll.cfg synce4l.conf

%build
%{make_build} \
	EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
	EXTRA_LDFLAGS="$RPM_LD_FLAGS"

%install
# make_install doesn't work here
%makeinstall

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_unitdir},%{_mandir}/man5}
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}
install -m 644 -p synce4l.conf $RPM_BUILD_ROOT%{_sysconfdir}

echo '.so man8/synce4l.8' > $RPM_BUILD_ROOT%{_mandir}/man5/synce4l.conf.5

%check
./synce4l -h 2>&1 | grep 'usage:.*synce4l'

%post
%systemd_post synce4l.service

%preun
%systemd_preun synce4l.service

%postun
%systemd_postun_with_restart synce4l.service

%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/synce4l.conf
%{_unitdir}/synce4l.service
%{_sbindir}/synce4l
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-6
- Prepare for Oreon 11 (RP1)
