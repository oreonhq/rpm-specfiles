%global source0_hash f0a7f8d84b529db000e2ba23fdd30980d0ef50c26b8ef780b36bfdf18cd67ba5
%global _hardened_build 1
Name: lprint
Version: 1.4.0
Release:        1%{?dist}
Summary:        A Label Printer Application
License: Apache-2.0
URL: https://www.msweet.org/lprint
Source0:        https://github.com/michaelrsweet/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: lprint.conf
Requires: filesystem
Requires: authselect-libs
Requires: avahi
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(pappl)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
LPrint is a label printer application for macOS and Linux. Basically,
LPrint is a print spooler optimized for label printing. It accepts
"raw" print data as well as PNG images (like those used for shipping
labels by most shippers' current web APIs) and has built-in "drivers"
to send the print data to USB and network-connected label printers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CC=%{__cc}
%set_build_flags
%configure 
%make_build
%install
%make_install DESTDIR=''
install -p -D -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/lprint.conf
%oreon_autofiles main

%pre

if [ $1 -gt 1 ]
then
    if test -f /var/lib/lprint.state
    then
        ! grep -q "^server-options" /var/lib/lprint.state || mv -f /var/lib/lprint.state /etc/lprint.conf
    fi
    if test ! -f /var/lib/lprint.state -a -f /etc/lprint.conf
    then
        grep -q "^server-options" /etc/lprint.conf || mv -f /etc/lprint.conf /var/lib/lprint.state
    fi
fi
%post

if test ! -f /var/lib/lprint.state
then
  touch /var/lib/lprint.state
fi
%systemd_post lprint.service
%preun

%systemd_preun lprint.service
%postun

%systemd_postun_with_restart lprint.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
