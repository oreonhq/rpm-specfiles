%global source0_hash e6140fd48c98a8b0c64b97fdada78f6ff3d3b25241d036fdced738257cb1ad39

Name:           ifm
Version:        5.5
Release:        3%{?dist}
Summary:        Interactive Fiction Mapper

License:        GPL-2.0-or-later
URL:            https://git.sr.ht/~zondo/ifm
Source0:        https://git.sr.ht/~zondo/ifm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ifm.sh
Patch1:         ifm-5.4-destdir.patch
Patch2:         0003-Rename-dumb-frotz-to-dfrotz.patch
# Submitted upstream to maintainer zondo42@gmail.com
Patch3:         ifm-5.5-libvars_vfuncs.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  tk
BuildRequires:  zlib-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  vim-filesystem
BuildRequires:  emacs-common

# For dfrotz, used by rec2scr.pl
Recommends:     frotz

%description
IFM is a language and a program for keeping track of your progress through
an Interactive Fiction game.  You can record each room you visit and its
relation to other rooms, the initial locations of useful items you find, and
the tasks you need to perform in order to solve the game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Do not attempt to run bison/yacc.
touch src/ifm-parse.c

%build
%configure
make %{?_smp_mflags}

%install
%make_install ifmdocdir=%{_pkgdocdir}
# Bash completion
install -p -D -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/bash_completion.d/ifm.sh
# Emacs mode
install -p -D -m 0644 contrib/ifm-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
# Vim syntax file
install -p -D -m 0644 contrib/ifm.vim %{buildroot}%{vimfiles_root}/syntax/%{name}.vim
# rec2scr.pl, a transcript-building tool included in contrib/
install -p -D -m 0755 contrib/rec2scr.pl %{buildroot}%{_bindir}/%{name}-rec2scr.pl

%files
%license COPYING
%{_pkgdocdir}
%{_bindir}/*
%{_datadir}/ifm/
%{_mandir}/man1/ifm.1*
%{_sysconfdir}/bash_completion.d/ifm.sh
%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
%{vimfiles_root}/syntax/%{name}.vim

%changelog
%autochangelog
