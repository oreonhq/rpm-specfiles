%global source0_hash c88086b5a926e8801154a0119de6a497a3891581a0219a0ef8d9d8e98556eb9b

%bcond_with sourcegit

Name:           llmnrd
Version:        0.7
Release:        16%{?dist}
Summary:        Link-Local Multicast Resolution Daemon

License:        GPL-2.0-only
URL:            https://github.com/tklauser/llmnrd
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        llmnrd.service

BuildRequires:  gcc
BuildRequires:  make
%if %{with sourcegit}
BuildRequires:  git-core
%endif
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
llmnrd is a daemon implementing the Link-Local Multicast Name Resolution (LLMNR)
protocol according to RFC 4795.

llmnrd will respond to name resolution queries sent by Windows clients in
networks where no DNS server is available. It supports both IPv4 and IPv6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%set_build_flags
%make_build prefix=%{_usr} Q= BINDIR=%{_bindir} SBINDIR=%{_sbindir}

%install
%make_install prefix=%{_usr} Q= BINDIR=%{_bindir} SBINDIR=%{_sbindir}
install -m 0644 -Dp %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/llmnrd.service

%check
# would not find result, but it tries
${RPM_BUILD_ROOT}%{_bindir}/llmnr-query -I lo localhost

%post
%systemd_post %{name}

%preun
%systemd_preun %{name}

%postun
%systemd_postun_with_restart %{name}

%files
%doc README*
%license COPYING
%{_bindir}/llmnr-query
%{_sbindir}/llmnrd
%{_unitdir}/llmnrd.service
%{_mandir}/man1/llmnr-query.1*
%{_mandir}/man8/llmnrd.8*

%changelog
%autochangelog
