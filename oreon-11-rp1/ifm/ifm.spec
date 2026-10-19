%global source0_hash b1dc195c6531d4bf08d0599aae0f204c18a30ad55bf4e11ca3aa1945c7097e3d
Name:           ifm
Version:        5.5
Release:        1%{?dist}
Summary:        Interactive Fiction Mapper
License:        GPL-2.0-or-later
URL:            https://git.sr.ht/~zondo/ifm
Source0:        https://git.sr.ht/~zondo/ifm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ifm.sh
Patch1:         ifm-5.4-destdir.patch
Patch2:         0003-Rename-dumb-frotz-to-dfrotz.patch
Patch3:         ifm-5.5-libvars_vfuncs.patch
Recommends:     frotz
# oreon:deps
BuildRequires:  automake
BuildRequires:  emacs-common
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  tk
BuildRequires:  vim-filesystem
BuildRequires:  zlib-devel
# /oreon:deps
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
install -p -D -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/bash_completion.d/ifm.sh
install -p -D -m 0644 contrib/ifm-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
install -p -D -m 0644 contrib/ifm.vim %{buildroot}%{vimfiles_root}/syntax/%{name}.vim
install -p -D -m 0755 contrib/rec2scr.pl %{buildroot}%{_bindir}/%{name}-rec2scr.pl
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
