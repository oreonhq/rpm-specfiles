%global source0_hash 9b7bc16f086479dcc626c575976568ba4a85d34297a750d8ab3d2e57f6d8b988

# Only enable if using patches that touches configure.ac,
# Makefile.am or other build system related files
#
Summary: An authorization framework
Name: polkit
Version: 127
Release: 3%{?dist}
License: LGPL-2.0-or-later
URL: https://github.com/polkit-org/polkit
Source0: https://github.com/polkit-org/polkit/archive/refs/tags/%{version}.tar.gz
Source1: polkit.sysusers

Patch1: 0001-polkit-agent-helper-service-simplify-sandbox-rules.patch
Patch2: 0002-agent-helper-Send-standard-error-to-journal.patch
Patch3: 0004-polkitsubject-Fix-GVariant-ref-leak-for-pidfd-withou.patch
Patch4: 0005-Aisle-www.aisle.com-reported-an-issue-with-unsanitiz.patch
Patch5: 0006-Add-Kazakh-translation.patch

BuildRequires: gcc-c++
BuildRequires: glib2-devel >= 2.30.0
BuildRequires: expat-devel
BuildRequires: pam-devel
BuildRequires: gtk-doc
BuildRequires: gettext-devel
BuildRequires: gobject-introspection-devel
BuildRequires: systemd, systemd-devel, systemd-rpm-macros
BuildRequires: dbus-devel
BuildRequires: pkgconfig(duktape)
BuildRequires: meson >= 1.4.0
BuildRequires: git

Requires: dbus
Recommends: polkit-pkla-compat
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}

Obsoletes: PolicyKit <= 0.10
Provides: PolicyKit = 0.11

# polkit saw some API/ABI changes from 0.96 to 0.97 so require a
# sufficiently new polkit-gnome package
Conflicts: polkit-gnome < 0.97

Obsoletes: polkit-desktop-policy < 0.103
Provides: polkit-desktop-policy = 0.103

Obsoletes: polkit-js-engine < 0.120-5
Provides: polkit-js-engine = %{version}-%{release}

# when -libs was split out, handle multilib upgrade path -- rex
Obsoletes: polkit < 0.113-3

%description
polkit is a toolkit for defining and handling authorizations.  It is
used for allowing unprivileged processes to speak to privileged
processes.

%package devel
Summary: Development files for polkit
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %name-docs = %{version}-%{release}
Requires: glib2-devel
Obsoletes: PolicyKit-devel <= 0.10
Provides: PolicyKit-devel = 0.11

%description devel
Development files for polkit.

%package docs
Summary: Development documentation for polkit
Requires: %name-devel = %{version}-%{release}
Obsoletes: PolicyKit-docs <= 0.10
Provides: PolicyKit-docs = 0.11
BuildArch: noarch

%description docs
Development documentation for polkit.

%package libs
Summary: Libraries for polkit

%description libs
Libraries files for polkit.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git

%build
%meson -D authfw=pam \
       -D examples=false \
       -D gtk_doc=true \
       -D introspection=true \
       -D man=true \
       -D session_tracking=logind \
       -D tests=false

%meson_build

%install
%meson_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/polkit.conf

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang polkit-1


%post
# The implied (systemctl preset) will fail and complain, but the macro hides
# and ignores the fact.  This is in fact what we want, polkit.service does not
# have an [Install] section and it is always started on demand.
%systemd_post polkit.service

%preun
%systemd_preun polkit.service

%postun
%systemd_postun_with_restart polkit.service

%files -f polkit-1.lang
%doc COPYING NEWS.md README.md
%{_datadir}/man/man1/*
%{_datadir}/man/man5/*
%{_datadir}/man/man8/*
%{_datadir}/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%{_datadir}/dbus-1/system-services/*
%{_unitdir}/polkit.service
%{_unitdir}/polkit-agent-helper.socket
%{_unitdir}/polkit-agent-helper@.service
%dir %{_datadir}/polkit-1/
%dir %{_datadir}/polkit-1/actions
%dir %{_datadir}/polkit-1/rules.d
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.policy
%{_datadir}/polkit-1/policyconfig-1.dtd
%{_datadir}/polkit-1/polkitd.conf
%dir %{_sysconfdir}/polkit-1
%{_datadir}/polkit-1/rules.d/50-default.rules
%attr(0750,root,polkitd) %dir %{_sysconfdir}/polkit-1/rules.d
%{_sysusersdir}/polkit.conf
%{_prefix}/lib/pam.d/polkit-1
%{_bindir}/pkaction
%{_bindir}/pkcheck
%{_bindir}/pkttyagent
%dir %{_prefix}/lib/polkit-1
%{_prefix}/lib/polkit-1/polkitd
%{_tmpfilesdir}/polkit-tmpfiles.conf

# see upstream docs for why these permissions are necessary
%attr(4755,root,root) %{_bindir}/pkexec
%attr(4755,root,root) %{_prefix}/lib/polkit-1/polkit-agent-helper-1

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_includedir}/*
%{_datadir}/gettext/its/polkit.its
%{_datadir}/gettext/its/polkit.loc

%files docs
%{_datadir}/gtk-doc

%ldconfig_scriptlets libs

%files libs
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/*.typelib

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 127-3
- Prepare for Oreon 11 (RP1)
