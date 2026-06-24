%global source0_hash none

Name:         amtterm
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:      GPL-2.0-or-later
Version:      1.6
Release:      26%{?dist}
Summary:      Serial-over-lan (sol) client for Intel AMT
URL:          http://www.kraxel.org/blog/linux/amtterm/
Source:       http://www.kraxel.org/releases/%{name}/%{name}-%{version}.tar.gz

Requires:     xdg-utils
Requires:     perl(SOAP::Lite)

BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: make

%description
Serial-over-lan (sol) client for Intel AMT.
Includes a terminal and a graphical (gtk) version.
Also comes with a perl script to gather informations
about and remotely control AMT managed computers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{set_build_flags}
make prefix=/usr

%install
make prefix=/usr DESTDIR=%{buildroot} STRIP="" install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/gamt.desktop

%files
%doc COPYING
%{_bindir}/amtterm
%{_bindir}/amttool
%{_bindir}/gamt
%{_mandir}/man1/amtterm.1.gz
%{_mandir}/man1/amttool.1.gz
%{_mandir}/man1/gamt.1.gz
%{_mandir}/man7/amt-howto.7.gz
%{_datadir}/applications/gamt.desktop

%changelog
%autochangelog

