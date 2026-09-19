%global source0_hash e0086c9b9811df2bdf763ec9016dfb1bcb7dba9fa6d7858725b0929069a12622

Name:           wol
Version:        0.7.1
Release:        39%{?dist}
Summary:        Wake On Lan client

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/wake-on-lan/
Source0:        http://downloads.sourceforge.net/wake-on-lan/%{name}-%{version}.tar.gz
Patch0:         wol-0.7.1-binding.patch
Patch1:         wol-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  perl-podlators

%description
wol implements Wake On LAN functionality in a small program. It wakes up
hardware that is Magic Packet compliant. SecureON is supported by wol too.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .binding
%patch -P1 -p1 -b .configure-c99

%build
export CFLAGS="$CFLAGS -std=gnu11"
%configure --disable-static
make %{?_smp_mflags}
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv
touch -c -r ChangeLog ChangeLog.conv
mv ChangeLog.conv ChangeLog

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_infodir}/%{name}.info.*
%{_mandir}/man?/*.*
%{_bindir}/%{name}*

%changelog
%autochangelog
