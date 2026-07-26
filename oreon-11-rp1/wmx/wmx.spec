%global source0_hash 4c727fd169c9643398c447078fd1e5f8a97a06da77ab2d06a6632abb9b1ad19a

Name: wmx
Version: 8
Release: 27%{?dist}
Summary: A really simple window manager for X
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.all-day-breakfast.com/wmx/
Source0: http://www.all-day-breakfast.com/wmx/%{name}-%{version}.tar.gz
Source1: wmx-defaults-3.tar.gz
Source2: background.xpm
Source3: wmx.desktop
Source4: Xclients.wmx.sh
Patch0: wmx-8-cfg.patch
#wmx's 'New' button is hardcoded to start an xterm, better make sure we have it:
Requires: xterm
BuildRequires: make
BuildRequires: gcc-c++ xorg-x11-proto-devel libX11-devel libXpm-devel libXext-devel libXaw-devel libXt-devel libXcomposite-devel freetype-devel libXft-devel

%description
A really simple window manager for X, based on wm2, with a minimal set of
configurable options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%setup -q -a 1
%{__install} -p -m 0644 %{SOURCE2} .
%patch -P0 -p1

%build
%configure --x-libraries=%{_libdir} --x-includes=%{_includedir}/X11 LIBS=-lfontconfig
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 wmx %{buildroot}%{_bindir}/wmx
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}
%{__install} -m 0755 wmx-defaults-3/* %{buildroot}%{_datadir}/%{name}
%{__chmod} 0644 %{buildroot}%{_datadir}/%{name}/startup
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/xsessions/wmx.desktop
%{__install} -D -m 0755 %{SOURCE4} %{buildroot}%{_sysconfdir}/X11/xinit/Xclients.d/Xclients.wmx.sh

%files
%doc README* UPDATES TODO.netwm rsharman-patch/
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/*
%{_sysconfdir}/X11/xinit/Xclients.d/*

%changelog
%autochangelog
