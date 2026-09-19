%global source0_hash 2cc88d4408d5c3fcdd06de2ddb9e330b8fd55eb5450f89f8333f44b0b86bc7b8

Name:           perl-pmtools
Version:        2.2.0
Release:        25%{?dist}
Summary:        A suite of small programs to help manage Perl modules

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/pmtools
Source:         https://cpan.metacpan.org/authors/id/M/ML/MLFISHER/pmtools-%{version}.tar.gz
# Adapt to Perl 5.26.0 POD changes, bug #1465062, CPAN RT#122210
Patch0:         pmtools-2.0.0-t_pfcat_5.26.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant) >= 1.01
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
BuildRequires:  perl(perlfaq)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This is pmtools -- a suite of small programs to help manage modules.
The names are totally preliminary, and in fact, so is the code.  We follow
the "keep it small" notion of many tiny tools each doing one thing well,
eschewing giant megatools with millions of options.

Tom Christiansen

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pmtools-%{version}
%patch -P 0 -p1
find . -type f -perm 755 | xargs perl -pi -MConfig -e 's{^#!/usr/bin/env perl}{$Config{startperl}}'
chmod -c a-x Changes TODO lib/Devel/Loaded.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{make_build}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# Default perl's pager less fails with /dev/null on stdin (bug #2208970)
export PAGER=/usr/bin/cat
make test

%files
%license LICENSE
%doc Changes README TODO
%{_bindir}/basepods
%{_bindir}/faqpods
%{_bindir}/modpods
%{_bindir}/pfcat
%{_bindir}/plxload
%{_bindir}/pm*
%{_bindir}/podgrep
%{_bindir}/podpath
%{_bindir}/pods
%{_bindir}/podtoc
%{_bindir}/sitepods
%{_bindir}/stdpods
%{perl_vendorlib}/Devel/
%{perl_vendorlib}/pmtools.pm
%{_mandir}/man1/basepods.1*
%{_mandir}/man1/faqpods.1*
%{_mandir}/man1/modpods.1*
%{_mandir}/man1/pfcat.1*
%{_mandir}/man1/plxload.1*
%{_mandir}/man1/pm*.1*
%{_mandir}/man1/podgrep.1*
%{_mandir}/man1/podpath.1*
%{_mandir}/man1/pods.1*
%{_mandir}/man1/podtoc.1*
%{_mandir}/man1/sitepods.1*
%{_mandir}/man1/stdpods.1*
%{_mandir}/man3/Devel::Loaded.3*
%{_mandir}/man3/pmtools.3*

%changelog
%autochangelog
