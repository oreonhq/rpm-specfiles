%global source0_hash 8b6f4f0d40bef5cfdfb7eb7c82ea1402d2747c37b2c7b7aa92faff55351df11d

Name:		gnurobots
Version:	1.2.0
Release:	43%{?dist}
Summary:	A robot programming game

License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/%{name}/
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-%{version}-guile.patch
Patch1:         pointer-types.patch

BuildRequires:  gcc
BuildRequires:	compat-guile18-devel >= 1.8 , readline-devel, vte-devel
BuildRequires:	desktop-file-utils
BuildRequires: make

%description

GNU Robots is a game/diversion where you construct a program for a little 
robot, then set him loose and watch him explore a world on his own.  
The robot program is written in Scheme, and is implemented using GNU Guile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p0 -b .guile
%patch -P 1 -p0 -b .pointers
sed -i.optflags -e '/^CFLAGS=/d' configure

%build

export GUILE=/usr/bin/guile1.8
export GUILE_CONFIG=/usr/bin/guile1.8-config
export GUILE_TOOLS=/usr/bin/guile1.8-tools
export CFLAGS="$CFLAGS -std=gnu17"

%configure
make %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}/xpm
%{__cp} -av xpm/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}/xpm/
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO doc/Robots-HOWTO
%attr(644,root,root) %{_datadir}/%{name}/scheme/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/maps/
%{_datadir}/%{name}/xpm/
%dir %{_datadir}/%{name}/scheme
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
