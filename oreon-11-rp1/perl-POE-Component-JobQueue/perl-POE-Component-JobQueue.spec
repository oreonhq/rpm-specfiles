%global source0_hash 396719160f4cbcbcf75036ae138c26fe7fea08a170d4bef4580f4dc557acf78e

Name:           perl-POE-Component-JobQueue
Version:        0.571
Release:        39%{?dist}
Summary:        Process a large number of tasks with a finite number of workers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-JobQueue
Source0: https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-JobQueue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE) >= 1.007
BuildRequires:  perl(POE::Session)
Requires:       perl(POE) >= 1.007

%description
POE::Component::JobQueue manages a finite pool of worker sessions as
they handle an arbitrarily large number of tasks.  It often is used as
a form of flow control, preventing an arbitrarily large number of
worker sessions from exhausting some finite resource.

%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-JobQueue-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
# readme says this is a good example.  So, why not?
cp t/01_queues.t example_01_queues
chmod -x example_01_queues

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc CHANGES README example_01_queues
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
