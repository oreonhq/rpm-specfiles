%global source0_hash 17cd2bf2212355473007c456eb2df9774b54ed08277fd141d6cc59512c873240

Name:           stalonetray
Version:        0.9.0
Release:        2%{?dist}
Summary:        A stand alone notification area

# License is only mentioned in COPYING
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://d3adb5.github.io/%{name}
Source0:        https://github.com/d3adb5/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libX11-devel

# Needed until upstream generates proper tarballs.
BuildRequires: autoconf automake docbook-xsl xsltproc

%description
The stalonetray is a STAnd-aLONE system TRAY (notification area).
It has minimal build and run-time dependencies: the Xlib only. The XEMBED
support is planned. Stalonetray runs under virtually any window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# https://github.com/kolbusa/stalonetray/issues/35
aclocal
autoheader
autoconf
automake --add-missing
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -D -m644 stalonetrayrc.sample %{buildroot}%{_sysconfdir}/stalonetrayrc

%files
%doc AUTHORS BUGS COPYING NEWS README.md TODO
%doc stalonetrayrc.sample stalonetray.html stalonetray.xml
%{_sysconfdir}/stalonetrayrc
%{_bindir}/stalonetray
%{_mandir}/man1/stalonetray.*

%changelog
%autochangelog
