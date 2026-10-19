%global source0_hash 6226fb76853ca94f37dd3fb74c3a99384c85e513bf4c3ea7a7ee5c43e9887d7e
%global gap_pkgname scscp
%global gap_upname  SCSCP
%global usrname     gapd
%global giturl      https://github.com/gap-packages/scscp
Name:           gap-pkg-%{gap_pkgname}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Symbolic Computation Software Composability Protocol in GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/scscp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
Source1:        %{usrname}.sh
Source2:        gap-scscp.service
Source3:        %{usrname}.logrotate
Source4:        %{usrname}.conf
Source5:        %{usrname}.h2m
Source6:        server.g
Source7:        %{name}.sysusers
Patch:          %{name}-makedoc.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): *.sh demo example lib par tracing tst
BuildOption(check): tst/testall.g
%{?systemd_requires}
Requires:       gap-pkg-io
Requires:       gap-pkg-openmath
Requires:       logrotate
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-openmath-doc
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  help2man
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package implements the Symbolic Computation Software Composability
Protocol (SCSCP) for the GAP system in accordance with the SCSCP
specification, described at https://openmath.org/standard/scscp/, and OpenMath
dictionaries scscp1 and scscp2.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SCSCP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-openmath-doc
Requires:       gap-pkg-smallgrp-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%install -a
cp -a doc/img %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc
install -p -m 0755 %{SOURCE1} %{buildroot}%{gap_libdir}/pkg/%{gap_upname}
mkdir -p %{buildroot}%{_sharedstatedir}/%{usrname}
mkdir -p %{buildroot}%{_sysusersdir}
cp -p %{SOURCE7} %{buildroot}%{_sysusersdir}/%{usrname}.conf
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 -p %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man8
help2man -m 'GAP SCSCP package' -S 'GAP SCSCP (Fedora %{version}-%{release})' \
  -n 'GAP Daemon' -I %{SOURCE5} -o %{buildroot}%{_mandir}/man8/%{usrname}.8 \
  -N -s 8 %{SOURCE1}
mkdir -p %{buildroot}%{_sysconfdir}/scscp/gap
install -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/scscp/gap
mv %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/config.g \
   %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/configpar.g \
   %{buildroot}%{_sysconfdir}/scscp/gap
ln -s %{_sysconfdir}/scscp/gap/config.g %{buildroot}%{gap_libdir}/pkg/%{gap_upname}
ln -s %{_sysconfdir}/scscp/gap/configpar.g %{buildroot}%{gap_libdir}/pkg/%{gap_upname}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd tst
gap --packagedirs ../.. << EOF
LoadPackage("scscp");
GAP_EXIT_CODE(Test("offline.tst", rec(compareFunction := "uptowhitespace") ));
EOF
cd -
%pre

%sysusers_create_package %{usrname} %{SOURCE7}
%preun

%systemd_preun gap-scscp.service
%post

%systemd_post gap-scscp.service
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-scscp-doc -f %{oreon_filedir}/gap-pkg-scscp-doc.list

%changelog

%autochangelog
