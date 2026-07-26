%global source0_hash 6547af61f3aa85793f8616190938d677d7995fb3b720c16258040bc935e2129f

Name:           perl-HTML-Template
Version:        2.97
Release:        28%{?dist}
Summary:        Perl module to use HTML Templates
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Template
Source0:        https://cpan.metacpan.org/modules/by-module/HTML/HTML-Template-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional Functionality
BuildRequires:  perl(GTop)
BuildRequires:  perl(IPC::SharedCache)
BuildRequires:  perl(Storable)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Suggests:       perl(GTop)
Suggests:       perl(IPC::SharedCache)
Suggests:       perl(Storable)

%description
This module attempts make using HTML templates simple and natural.  It
extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>.  The file
written with HTML and these new tags is called a template.  It is
usually saved separate from your script - possibly even created by
someone else!  Using this module you fill in the values for the
variables, loops and branches declared in the template.  This allows
you to separate design - the HTML - from the data, which you generate
in the Perl script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Template-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
TEST_SHARED_MEMORY=1 make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/HTML/
%{_mandir}/man3/HTML::Template.3*
%{_mandir}/man3/HTML::Template::FAQ.3*

%changelog
%autochangelog
