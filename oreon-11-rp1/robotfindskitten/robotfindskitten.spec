%global source0_hash bc199c96a0a2ef79621b548d0f223bd8dce5cff798b7277708e31037e32df9fb
Name:      robotfindskitten
Version:   2.8284271.702
Release:        16%{?dist}
Summary:        A game/zen simulation. You are robot. Your job is to find kitten.
License:   GPL-2.0-or-later
URL:       http://robotfindskitten.org
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:    robotfindskitten-2.8284271.702-maybe-uninitialized.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  texinfo
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
