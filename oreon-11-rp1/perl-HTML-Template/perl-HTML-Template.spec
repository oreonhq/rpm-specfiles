%global source0_hash 6547af61f3aa85793f8616190938d677d7995fb3b720c16258040bc935e2129f
Name:           perl-HTML-Template
Version:        2.97
Release:        28%{?dist}
Summary:        Perl module to use HTML Templates
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Template
Source0:        https://cpan.metacpan.org/modules/by-module/HTML/HTML-Template-%{version}.tar.gz
BuildArch:      noarch
Suggests:       perl(GTop)
Suggests:       perl(IPC::SharedCache)
Suggests:       perl(Storable)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(GTop)
BuildRequires:  perl(IPC::SharedCache)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

TEST_SHARED_MEMORY=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
