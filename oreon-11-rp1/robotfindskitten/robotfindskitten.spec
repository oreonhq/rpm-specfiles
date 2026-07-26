%global source0_hash bc199c96a0a2ef79621b548d0f223bd8dce5cff798b7277708e31037e32df9fb

Name:      robotfindskitten
Version:   2.8284271.702
Release:   16%{?dist}
Summary:   A game/zen simulation. You are robot. Your job is to find kitten.

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       http://robotfindskitten.org
Source0:   https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:    robotfindskitten-2.8284271.702-maybe-uninitialized.patch

BuildRequires: make
BuildRequires: ncurses-devel glibc-devel texinfo autoconf automake libtool

%description
In this game, you are robot (#). Your job is to find kitten. This task
is complicated by the existence of various things which are not kitten.
Robot must touch items to determine if they are kitten or not. The game
ends when robotfindskitten.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -i

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make -C nki install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
ln -sf ../games/robotfindskitten $RPM_BUILD_ROOT/%{_bindir}/robotfindskitten
# make install creates this, but we don't need it
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%doc AUTHORS BUGS ChangeLog COPYING NEWS README
%{_bindir}/robotfindskitten
%{_prefix}/games/robotfindskitten
%{_datadir}/games/robotfindskitten/
%{_datadir}/info/robotfindskitten.info*
%{_datadir}/man/man6/robotfindskitten.6*

%changelog
%autochangelog
