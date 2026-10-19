%global source0_hash 4381994b998a0b41e3b27d532bdb2a859fefaca260705022eeec8c1c02e99680
Summary:        Completely configurable key-combo grabber for blackbox
Name: bbkeys
Version: 0.9.1
Release:        1%{?dist}
License: MIT
URL: http://bbkeys.sourceforge.net/
Source0:        http://downloads.sf.net/bbkeys/bbkeys-%{version}.tar.gz
Patch0: bbkeys-0.9.0-gcc43.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  blackbox-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
bbkeys is a configurable key-grabber designed for the blackbox window manager
which is written by Brad Hughes.  It is based on the bbtools object code
created by John Kennis and re-uses some of the blackbox window manager classes
as well.  bbkeys is easily configurable via directly hand-editing the user's
~/.bbkeysrc file, or by using the GUI total blackbox configurator, bbconf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vi
%configure --datadir=%{_sysconfdir}
%make_build
%install
%make_install
%{__rm} -rf %{buildroot}%{_sysconfdir}/doc/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
