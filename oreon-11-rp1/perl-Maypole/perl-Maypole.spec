%global source0_hash 5f75a5a710cedcb6276219eb4ce3226c41f5dba72e9cabe68973a66c511ce69c
Name:		perl-Maypole
Version:	2.13
Release:        1%{?dist}
Epoch:		1
Summary:        MVC web application framework
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://maypole.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/T/TE/TEEJAY/Maypole-%{version}.tar.gz
BuildArch:	noarch
Requires:	mod_perl
# oreon:deps
BuildRequires:  libapreq2-devel
BuildRequires:  make
BuildRequires:  mod_perl
BuildRequires:  perl(Apache2::Request)
BuildRequires:  perl(Apache::Session::Wrapper)
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(CGI::Untaint::date)
BuildRequires:  perl(CGI::Untaint::email)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Class::DBI::AbstractSearch)
BuildRequires:  perl(Class::DBI::AsForm)
BuildRequires:  perl(Class::DBI::FromCGI)
BuildRequires:  perl(Class::DBI::Loader)
BuildRequires:  perl(Class::DBI::Loader::Relationship)
BuildRequires:  perl(Class::DBI::Pager)
BuildRequires:  perl(Class::DBI::Plugin::RetrieveAll)
BuildRequires:  perl(Class::DBI::SQLite)
BuildRequires:  perl(Class::DBI::mysql)
BuildRequires:  perl(File::MMagic::XS)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(IO::CaptureOutput)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Plugin::Class)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
%description
Maypole is a Perl framework for MVC-oriented web 
applications, similar to Jakarta's Struts. Maypole 
is designed to minimize coding requirements for 
creating simple web interfaces to databases, while 
remaining flexible enough to support enterprise web 
applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Maypole-%{version}

# Filter false positive requires
cat <<EOF > %{name}-req
#!/bin/sh
%{__perl_requires} \
| grep -v 'perl(mod_perl)'
EOF
%global __perl_requires %{_builddir}/Maypole-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
