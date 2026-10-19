%global source0_hash b0b56e08c0d6dee5ad98270cdede05ff68b9c2be05fc25ebcaddd70c52ab8766
Name:           ppc64-diag
Version:        2.7.11
Release:        1%{?dist}
Summary:        PowerLinux Platform Diagnostics
URL:            https://github.com/power-ras/%{name}
License:        GPL-2.0-only
ExclusiveArch:  ppc %{power64}
Requires:       ppc64-diag-rtas >= 2.7.6
Requires:       servicelog
Requires:       lsvpd
Requires:       powerpc-utils >= 1.3.0
Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        add_regex.8
Source2:        convert_dt_node_props.8
Source3:        extract_opal_dump.8
Source4:        extract_platdump.8
Source5:        rtas_errd.8
Patch0:         ppc64-diag-2.7.9-fedora.patch
Patch1:         ppc64-diag-define.patch
Patch10:        ppc64-diag-2.7.0-diag_vnme-add-power11-support.patch
Patch11:        ppc64-diag-2.7.10-stdbool.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  librtas-devel
BuildRequires:  libservicelog-devel
BuildRequires:  libtool
BuildRequires:  libvpd-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
This package contains various diagnostic tools for PowerLinux.
These tools captures the diagnostic events from Power Systems
platform firmware, SES enclosures and device drivers, and
write events to servicelog database. It also provides automated
responses to urgent events such as environmental conditions and
predictive failures, if appropriate modifies the FRUs fault
indicator(s) and provides event notification to system
administrators or connected service frameworks.

%package        rtas
Summary:        rtas_errd daemon
Requires:       powerpc-utils-core >= 1.3.7-5
%description rtas
This package contains only rtas_errd daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
CXXFLAGS="%{build_cflags}" %configure
LDFLAGS="%{build_ldflags}" CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cflags}" make %{?_smp_mflags} V=1
%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 COPYING
rm -f $RPM_BUILD_ROOT%{_docdir}/ppc64-diag/*
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/ses_pages
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log/dump
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log/opal-elog
ln -sfv %{_sbindir}/usysattn $RPM_BUILD_ROOT/%{_sbindir}/usysfault
install -m 644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT/%{_mandir}/man8/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{_libexecdir}/%{name}/lp_diag_setup --register >/dev/null 2>&1
%{_libexecdir}/%{name}/ppc64_diag_setup --register >/dev/null 2>&1
if [ "$1" = "1" ]; then # first install
    systemctl -q enable opal_errd.service >/dev/null
    systemctl start opal_errd.service >/dev/null
elif [ "$1" = "2" ]; then # upgrade
    systemctl restart opal_errd.service >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi
%preun

if [ "$1" = "0" ]; then # last uninstall
    systemctl stop opal_errd.service >/dev/null
    systemctl -q disable opal_errd.service
    %{_libexecdir}/%{name}/ppc64_diag_setup --unregister >/dev/null
    %{_libexecdir}/%{name}/lp_diag_setup --unregister >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi
%triggerin -- librtas

if [ "$2" = "2" ]; then
    systemctl restart opal_errd.service >/dev/null
    systemctl restart rtas_errd.service >/dev/null
fi
%post rtas

if [ "$1" = "1" ]; then # first install
    systemctl -q enable rtas_errd.service >/dev/null
    systemctl start rtas_errd.service >/dev/null
elif [ "$1" = "2" ]; then # upgrade
    systemctl restart rtas_errd.service >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi
%preun rtas

if [ "$1" = "0" ]; then # last uninstall
    systemctl stop rtas_errd.service >/dev/null
    systemctl -q disable rtas_errd.service
    systemctl daemon-reload > /dev/null 2>&1
fi
%files -f %{oreon_filedir}/main.list
%files -n ppc64-diag-rtas -f %{oreon_filedir}/ppc64-diag-rtas.list

%changelog

%autochangelog
