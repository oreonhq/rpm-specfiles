%global source0_hash c6560ba645652eab0b16d46c9dbd8e5c9881c1f9d3ac6fa3da2ee3c865b5e6a0

Name:           wmctrl
Version:        1.07
Release:        41%{?dist}
Summary:        Command line tool to interact with an X Window Manager

License:        GPL-2.0-or-later
# URL and Source URL is dead now.
# New hosting can be used as https://github.com/Conservatory/wmctrl
URL:            http://sweb.cz/tripie/utils/wmctrl
Source0:        http://sweb.cz/tripie/utils/wmctrl/dist/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libXmu-devel
BuildRequires:  xorg-x11-proto-devel
Patch0:         http://ftp.de.debian.org/debian/pool/main/w/wmctrl/wmctrl_1.07-6.diff.gz
Patch1:         wmctrl-sticky-workspace.patch

%description
The wmctrl program is a UNIX/Linux command line tool to interact with an
EWMH/NetWM compatible X Window Manager. The tool provides command line access
to almost all the features defined in the EWMH specification. It can be used,
for example, to obtain information about the window manager, to get a detailed
list of desktops and managed windows, to switch and resize desktops, to make
windows full-screen, always-above or sticky, and to activate, close, move,
resize, maximize and minimize them. The command line access to these window
management functions makes it easy to automate and execute them from any
application that is able to run a command in response to an event.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
