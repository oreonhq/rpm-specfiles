%global source0_hash f467a2ef904e93e258d4d7bd2ad56c5c128796d395071fefef1d18053b6defcc
Name:		consolation
Version:	0.0.10
Release:        1%{?dist}
Summary:        Copy-paste for the Linux console
License:	GPL-2.0-or-later
URL:		https://salsa.debian.org/consolation-team/consolation/
Source0:        https://salsa.debian.org/consolation-team/consolation/-/archive/consolation-%{version}/%{name}-consolation-%{version}.tar.gz
Requires:	systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libinput-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
