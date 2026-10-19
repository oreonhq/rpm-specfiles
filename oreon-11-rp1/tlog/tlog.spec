%global source1_hash 4a485937bd7d1c3b0df971095a9c782c84bd9d04c52c5e550e8f1060a2fcab12
%global source0_hash 8613a4ba7267b876f7017ce17dfbcce95baced39df007b831c685cccc3342f6e
%global _hardened_build 1
%if 0%{?rhel} && 0%{?rhel} < 7 || (0%{?oreon} >= 11)
%bcond_with systemd
%else
%bcond_without systemd
%endif
%if "%{_vendor}" == "debbuild"
%global _defaultdocdir /usr/share/doc/%{name}
%global _buildshell /bin/bash
%global _lib lib/%(%{__dpkg_architecture} -qDEB_HOST_MULTIARCH)
%endif
%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}
%{!?make_build:%global make_build %{__make} %{?_smp_mflags}}
Name:           tlog
Version:        14
Release:        7%{?dist}
Summary:        Terminal I/O logger
%if "%{_vendor}" == "debbuild"
Packager:       Justin Stephenson <jstephen@redhat.com>
Group:          admin
License:        GPL-2.0+
%else
Group:          Applications/System
License:        GPL-2.0-or-later
%endif
URL:            https://github.com/Scribery/%{name}
Source0:        https://github.com/Scribery/tlog/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Scribery/%{name}/HEAD/tlog.sysusers
Patch0001: 0001-Add-missing-argument-for-sigchld-handler.patch
%if "%{_vendor}" == "debbuild"
%if %{with systemd}
Requires:         systemd-sysv
Requires(preun):  systemd
Requires(post):   systemd
Requires(postun): systemd
%endif
%else
%if %{defined suse_version}
%else
%endif
%if %{with systemd}
%{?systemd_requires}
%endif
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libutempter-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libsystemd)
# /oreon:deps
%description
Tlog is a terminal I/O recording program similar to "script", but used in
place of a user's shell, starting the recording and executing the real user's
shell afterwards. The recorded I/O can then be forwarded to a logging server
in JSON format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure --disable-rpath --disable-static --enable-utempter %{!?with_systemd:--disable-journal} --docdir=%{_defaultdocdir}/%{name}
%make_build
%check

%make_build check
%install
%make_install
rm %{buildroot}/%{_libdir}/*.la
rm %{buildroot}/%{_libdir}/*.so
rm -r %{buildroot}/usr/include/%{name}
%if %{with systemd}
    mkdir -p %{buildroot}%{_tmpfilesdir}
    {
        echo "# Type Path Mode UID GID Age Argument"
        echo "d /run/%{name} 0755 %{name} %{name}"
    } > %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
    mkdir -p %{buildroot}%{_localstatedir}/run
    install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}
%endif
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main

%post

/sbin/ldconfig
%if 0%{?el7} || 0%{?suse_version} >= 1315
%tmpfiles_create %{name}.conf
%endif
%if 0%{?ubuntu} || 0%{?debian}
systemd-tmpfiles --create %{name}.conf >/dev/null 2>&1 || :
%endif
%postun

/sbin/ldconfig
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14-7
- Import
