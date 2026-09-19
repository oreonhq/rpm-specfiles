%global source0_hash 5c860385ceed8a60f13217cc0192c4c2b4705c3e80f9866f7d72ff306eb72961

# typespeed.h included in multiple *.c files that are compiled separately
# upstream is inactive so this is probably not worth fixing
%define _legacy_common_support 1

Name:           typespeed
Version:        0.6.5
Release:        34%{?dist}
Summary:        Test your typing speed and get your fingers' CPS

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://typespeed.sourceforge.net/
Source0:        http://typespeed.sourceforge.net/typespeed-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires: make
BuildRequires:  gcc
BuildRequires: ncurses-devel gettext desktop-file-utils

%description
Typespeed gives your fingers' cps (total and correct), typoratio and
some points to compare with your friends.

Typespeed's idea is ripped from ztspeed (a DOS game made by
Zorlim). The idea behind the game is rather easy: type words that are
flying by from left to right as fast as you can. If you miss 10 or
more words, game is over.

You can play typespeed for your own or with a friend using TCP/IPv4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
iconv -f ISO88591 -t UTF8 ChangeLog -o ChangeLog

%build
%configure
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %{name}

desktop-file-install  \
                     --dir=$RPM_BUILD_ROOT/%{_datadir}/applications/ \
  %{SOURCE1}

%files -f %{name}.lang
%license COPYING
%doc BUGS ChangeLog NEWS README TODO
%attr(2755,root,games) %{_bindir}/%{name}
%attr(664,root,games) %config(noreplace) %{_localstatedir}/games/%{name}.score
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/doc/%{name}/README
%{_mandir}/man6/*

%changelog
%autochangelog
