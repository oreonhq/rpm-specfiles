%global source0_hash 5e8e725db97e91cf4d14f82c1d75b45428b6f972eb4e5bd695e5aeefcad3686b

%global _hardened_build 1

%if 0%{?rhel} && 0%{?rhel} < 7 || (0%{?oreon} >= 11)
# If it's RHEL6 and older
%bcond_with systemd
%else
%bcond_without systemd
%endif

%if "%{_vendor}" == "debbuild"
# Set values to make debian builds work well
%global _defaultdocdir /usr/share/doc/%{name}
%global _buildshell /bin/bash
%global _lib lib/%(%{__dpkg_architecture} -qDEB_HOST_MULTIARCH)
%endif

# Compatibility macros
%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}
%{!?make_build:%global make_build %{__make} %{?_smp_mflags}}

Name:           tlog
Version:        14
Release:        7%{?dist}
Summary:        Terminal I/O logger

%if "%{_vendor}" == "debbuild"
# Required for Debian
Packager:       Justin Stephenson <jstephen@redhat.com>
Group:          admin
License:        GPL-2.0+
%else
Group:          Applications/System
License:        GPL-2.0-or-later
%endif

URL:            https://github.com/Scribery/%{name}
Source0:        https://github.com/Scribery/tlog/releases/download/v14/tlog-14.tar.gz
Source1:        tlog.sysusers

Patch0001: 0001-Add-missing-argument-for-sigchld-handler.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  gcc
BuildRequires:  make

%if "%{_vendor}" == "debbuild"
BuildRequires:  libjson-c-dev
BuildRequires:  libcurl4-gnutls-dev
BuildRequires:  libutempter-dev
# Debian/Ubuntu doesn't automatically pull this in...
BuildRequires:  pkg-config

%if %{with systemd}
BuildRequires:  libsystemd-dev
# Expanded form of systemd_requires macro
Requires:         systemd-sysv
Requires(preun):  systemd
Requires(post):   systemd
Requires(postun): systemd
%endif

%else
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
%if %{defined suse_version}
BuildRequires:  utempter-devel
%else
BuildRequires:  libutempter-devel
%endif

%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd)
%{?systemd_requires}
%endif
%endif

%description
Tlog is a terminal I/O recording program similar to "script", but used in
place of a user's shell, starting the recording and executing the real user's
shell afterwards. The recorded I/O can then be forwarded to a logging server
in JSON format.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure --disable-rpath --disable-static --enable-utempter %{!?with_systemd:--disable-journal} --docdir=%{_defaultdocdir}/%{name}
%make_build

%check
%make_build check

%install
%make_install
rm %{buildroot}/%{_libdir}/*.la

# Remove development files as we're not doing a devel package yet
rm %{buildroot}/%{_libdir}/*.so
rm -r %{buildroot}/usr/include/%{name}

%if %{with systemd}
    # Create tmpfiles.d configuration for the lock dir
    mkdir -p %{buildroot}%{_tmpfilesdir}
    {
        echo "# Type Path Mode UID GID Age Argument"
        echo "d /run/%{name} 0755 %{name} %{name}"
    } > %{buildroot}%{_tmpfilesdir}/%{name}.conf
# Else, if it's RHEL6 or older
%else
    # Create the lock dir
    mkdir -p %{buildroot}%{_localstatedir}/run
    install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}
%endif

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%files
%{!?_licensedir:%global license %doc}
%license COPYING
%doc %{_defaultdocdir}/%{name}
%{_bindir}/%{name}-rec
%attr(6755,%{name},%{name}) %{_bindir}/%{name}-rec-session
%{_bindir}/%{name}-play
%{_libdir}/lib%{name}.so*
%{_datadir}/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
%if %{with systemd}
%{_tmpfilesdir}/%{name}.conf
%else
# If it's RHEL6 and older
%dir %attr(-,%{name},%{name}) %{_localstatedir}/run/%{name}
%endif
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-rec.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-rec-session.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-play.conf
%{_sysusersdir}/%{name}.conf


%post
/sbin/ldconfig
%if 0%{?el7} || 0%{?suse_version} >= 1315
# For RHEL7 and SUSE Linux distributions, creation doesn't happen automatically
%tmpfiles_create %{name}.conf
%endif
%if 0%{?ubuntu} || 0%{?debian}
# For Debian/Ubuntu, creation doesn't happen automatically
systemd-tmpfiles --create %{name}.conf >/dev/null 2>&1 || :
%endif

%postun
/sbin/ldconfig

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14-7
- Import
