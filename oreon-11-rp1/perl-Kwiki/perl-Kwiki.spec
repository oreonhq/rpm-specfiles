%global source0_hash c2c5e583dee9b0616239523ec79f1162c54e6114099de0f8c72b6947b382672c

Name:           perl-Kwiki
Version:        0.39
Release:        56%{?dist}
Summary:        Kwiki Wiki Building Framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-%{version}.tar.gz
Patch0:         Kwiki-0.39-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
# XXX: BuildRequires:  perl(CPAN)
BuildRequires:  perl(HTTP::BrowserDetect)
# This is actually Spiffy::mixin, the namespace is loaded via Spoon::Config
# XXX: BuildRequires:  perl(mixin)
BuildRequires:  perl(Spoon) >= 0.22
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
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(IO::All)
BuildRequires:  perl(lib)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Memory::Cycle)
Requires:       perl(CPAN)
Requires:       perl(Cwd)

# This is actually Spiffy::mixin; it's all rather obscure
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(mixin\\)$

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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
