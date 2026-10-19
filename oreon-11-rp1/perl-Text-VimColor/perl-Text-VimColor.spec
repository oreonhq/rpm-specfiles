%global source0_hash e20d3202c888af3d082a2245db5e87ee774e96fcf6708a30530f2eeb1a90988e
Name:           perl-Text-VimColor
Version:        0.29
Release:        1%{?dist}
Summary:        Syntax color text in HTML or XML using Vim
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-VimColor
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Text-VimColor-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Path::Class) >= 0.04
Requires:       perl(Term::ANSIColor) >= 1.03
Requires:       vim-enhanced
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Path::Class\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::StdHandle)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  vim-enhanced
# /oreon:deps
%description
This module tries to markup text files according to their syntax. It can be
used to produce web pages with pretty-printed colorful source code samples.
It can produce output in various formats. text-vimcolor is a command line
interface to the Perl module Text::VimColor:
  text-vimcolor --format html --filetype prolog foo.pl > foo.html

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-VimColor-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
