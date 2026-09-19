%global source0_hash 13c3fe5f430eb0c010560c7e438123a573ca61a55c6708aa750cfbf56bf25e17

Name:		gnujump
Version:	1.0.8
Release:	30%{?dist}
Summary:	A jumping game which is a clone of xjump

License:	GPL-3.0-or-later
URL:		http://gnu.org/software/%{name}
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch1:		%{name}-Makefile.in.patch

BuildRequires:  gcc
BuildRequires:	SDL-devel >= 1.2, SDL_mixer-devel, SDL_image-devel
BuildRequires:	desktop-file-utils
BuildRequires: make

%description
GNUjump is a clone of the simple yet addictive game Xjump, adding new features
like multiplaying, unlimited FPS, smooth floor falling, themable graphics,
sounds,replays, etc.

The goal in this game is to jump to the next floor trying not to fall down. As
you go upper in the Falling Tower the floors will fall faster. Try to survive 
longer get upper than anyone. It might seem too simple but once you've tried 
you'll realize how addictive this is. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p0 -b .orig

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%find_lang gnujump

%files -f gnujump.lang
%doc AUTHORS ABOUT-NLS COPYING README 
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
