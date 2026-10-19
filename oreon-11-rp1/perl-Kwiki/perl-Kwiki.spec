%global source0_hash c2c5e583dee9b0616239523ec79f1162c54e6114099de0f8c72b6947b382672c
Name:           perl-Kwiki
Version:        0.39
Release:        1%{?dist}
Summary:        Kwiki Wiki Building Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-%{version}.tar.gz
Patch0:         Kwiki-0.39-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
Requires:       perl(CPAN)
Requires:       perl(Cwd)
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(mixin\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::BrowserDetect)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Spoon)
BuildRequires:  perl(Spoon::Base)
BuildRequires:  perl(Spoon::CGI)
BuildRequires:  perl(Spoon::Command)
BuildRequires:  perl(Spoon::Config)
BuildRequires:  perl(Spoon::ContentObject)
BuildRequires:  perl(Spoon::Cookie)
BuildRequires:  perl(Spoon::Formatter)
BuildRequires:  perl(Spoon::Formatter::Block)
BuildRequires:  perl(Spoon::Formatter::Container)
BuildRequires:  perl(Spoon::Formatter::Phrase)
BuildRequires:  perl(Spoon::Formatter::Unit)
BuildRequires:  perl(Spoon::Hub)
BuildRequires:  perl(Spoon::Installer)
BuildRequires:  perl(Spoon::MetadataObject)
BuildRequires:  perl(Spoon::Plugin)
BuildRequires:  perl(Spoon::Registry)
BuildRequires:  perl(Spoon::Template)
BuildRequires:  perl(Spoon::Template::TT2)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A Wiki is a website that allows its users to add pages, and edit any
existing pages. It is one of the most popular forms of web collaboration.
If you are new to wiki, visit http://c2.com/cgi/wiki?WelcomeVisitors
which is possibly the oldest wiki, and has lots of information about how
wikis work.

Kwiki is a Perl wiki implementation based on the Spoon application
architecture and using the Spiffy object orientation model. The major goals
of Kwiki are that it be easy to install, maintain and extend.

All the features of a Kwiki wiki come from plugin modules. The base
installation comes with the bare minimum plugins to make a working Kwiki.
To make a really nice Kwiki installation you need to install additional
plugins. Which plugins you pick is entirely up to you. Another goal of
Kwiki is that every installation will be unique. When there are hundreds of
plugins available, this will hopefully be the case.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
