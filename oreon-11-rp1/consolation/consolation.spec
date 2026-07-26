%global source0_hash 8137ff21f8f818faf0de634e531dfe3ebec5e161f6be3b02e0d89ccf3796c45e

Name:		consolation
Version:	0.0.7
Release:	17%{?dist}
Summary:	Copy-paste for the Linux console

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://salsa.debian.org/consolation-team/consolation/
Source0:	https://salsa.debian.org/consolation-team/consolation/-/archive/consolation-%{version}/%{name}-consolation-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libinput-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:  pkgconfig(libinput) >= 1.5
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libevdev) >= 0.4
Requires:	systemd

%description
Consolation is a daemon that provide copy-paste and scrolling support to
the Linux console.

It is based on the libinput library and supports all pointer devices and
settings provided by this library,

Similar software include gpm and jamd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-consolation-%{version}

%build
autoreconf -fi
%configure
# Need to build the binary first, then the manual, otherwise the manual
# ends up butchered by the messed up make rules.
make %{?_smp_mflags} -C src consolation
make %{?_smp_mflags} consolation.8
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_unitdir}
install -pm644 consolation.service %{buildroot}%{_unitdir}

%systemd_post consolation.service
%systemd_preun consolation.service
%systemd_postun consolation.service

%files
%{_sbindir}/consolation
%{_mandir}/man8/consolation.8*
%{_unitdir}/consolation.service
%license LICENSE
%doc README AUTHORS ChangeLog

%changelog
%autochangelog
