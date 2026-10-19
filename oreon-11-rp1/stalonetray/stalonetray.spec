%global source0_hash aee903c391446c46f2d1f0a33aef815b55d1bfe8043ba283e5df01c829b481a8
Name:           stalonetray
Version:        1.5.0
Release:        1%{?dist}
Summary:        A stand alone notification area
License:        GPL-2.0-or-later
URL:            https://d3adb5.github.io/%{name}
Source0:        https://github.com/d3adb5/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  xsltproc
# /oreon:deps
%description
The stalonetray is a STAnd-aLONE system TRAY (notification area).
It has minimal build and run-time dependencies: the Xlib only. The XEMBED
support is planned. Stalonetray runs under virtually any window manager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

aclocal
autoheader
autoconf
automake --add-missing
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -D -m644 stalonetrayrc.sample %{buildroot}%{_sysconfdir}/stalonetrayrc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
