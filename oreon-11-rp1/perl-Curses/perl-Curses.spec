%global source0_hash 9631d6e3e2859c85913d8b8724f61fbebb9e932e9e50aa0493a4e0276660a3f9
Name:           perl-Curses
Version:        1.46
Release:        1%{?dist}
Summary:        Perl bindings for ncurses
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Curses
Source0:        https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/Curses-%{version}.tar.gz
Provides:       perl(Curses)
Provides:       perl(Curses)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Perl bindings for ncurses, bringing terminal-independent character
handling capabilities to Perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Curses-%{version}
test -f hints/c-linux.ncursesw.h || cp hints/c-linux.ncurses.h hints/c-linux.ncursesw.h
sed -i -e 's|/usr/local/bin/perl|%{__perl}|' demo*
sed -i -e 's|/usr//bin/perl|%{__perl}|' demo*

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
   PANELS MENUS FORMS
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
chmod -x demo*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
