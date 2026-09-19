%global source0_hash aa0bbd5a6b63c62c8955f8c55ec085e370d792d65266b6c3b5c5f0788bbc77e6

Name:           perl-HTML-Mason
Version:        1.60
Release:        9%{?dist}
Epoch:          1
Summary:        Powerful Perl-based web site development and delivery engine
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.masonhq.com/
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/HTML-Mason-%{version}.tar.gz
Source1:        perl-HTML-Mason.conf
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Stick to Apache2, ignore Apache 1 modules
BuildRequires:  perl(Apache2::Directive)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Cache::Cache) >= 1
BuildRequires:  perl(CGI) >= 2.46
BuildRequires:  perl(CHI) >= 0.21
BuildRequires:  perl(Class::Container) >= 0.07
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class) >= 1.15
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Log::Any) >= 0.08
BuildRequires:  perl(mod_perl2)
BuildRequires:  perl(Params::Validate) >= 0.70
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(vars)
BuildRequires:  perl(YAML)
# Tests:
# Apache not used
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Config)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Module::Build)
# Pod::Wordlist not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.88
# Test::NoTabs not used
# Test::Pod 1.41 not used
# Test::Spelling 0.12 not used
# Optional tests:
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Output)
Requires:       httpd-filesystem
# Stick to Apache2, ignore Apache 1 modules
Requires:       perl(Apache2::Directive)
Requires:       perl(Apache2::Log)
Requires:       perl(Apache2::RequestIO)
Requires:       perl(Apache2::RequestRec)
Requires:       perl(Apache2::RequestUtil)
Requires:       perl(Apache2::ServerUtil)
Requires:       perl(APR::Table)
Requires:       perl(Cache::Cache) >= 1
Requires:       perl(CHI) >= 0.21
Requires:       perl(Class::Container) >= 0.07
Requires:       perl(Exception::Class) >= 1.15
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(mod_perl2)
Requires:       perl(Params::Validate) >= 0.70
Requires:       perl(Scalar::Util) >= 1.01
Requires:       perl(YAML)

%{?perl_default_filter}

# Filter out under-specified Requires:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Container|Exception::Class|File::Spec|Params::Validate)\\)$

%description
Mason is a powerful Perl-based web site development and delivery
engine. With Mason you can embed Perl code in your HTML and construct
pages from shared, reusable components.  Mason solves the common
problems of site development: caching, debugging, templating,
maintaining development and production sites, and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Mason-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

rm -f $RPM_BUILD_ROOT%{_bindir}/*.README
for file in $RPM_BUILD_ROOT%{_bindir}/convert*.pl ; do
    mv -f $file $( echo $file | sed 's,/\(convert.*\)\.pl$,/mason_\1,' )
done
mv -f $RPM_BUILD_ROOT%{_bindir}/mason.pl $RPM_BUILD_ROOT%{_bindir}/mason

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/

# Apache:: (Apache1) module
# Not applicable on Fedora.
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/Mason/Apache

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/www/mason
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mason

%check
%{make_build} test

%files
%doc Changes CREDITS README.md UPGRADE
%license LICENSE
%doc eg/ samples/
%{_bindir}/mason*
%{perl_vendorlib}/*
%{_mandir}/man3/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/perl-HTML-Mason.conf
%dir %attr(775,root,apache) %{_localstatedir}/cache/mason
%dir %{_localstatedir}/www/mason

%changelog
%autochangelog
