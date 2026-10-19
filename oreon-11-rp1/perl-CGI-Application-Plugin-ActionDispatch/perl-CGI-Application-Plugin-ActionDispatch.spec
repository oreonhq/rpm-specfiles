%global source0_hash 0795c7fd5edcf1f64f34caada00d728f257189ec6073fe5d9379f1f51842a3ba
Name:           perl-CGI-Application-Plugin-ActionDispatch
Version:        0.99
Release:        1%{?dist}
Summary:        Adds attribute based support for parsing the PATH_INFO of an HTTP request
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-ActionDispatch
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JAYWHY/CGI-Application-Plugin-ActionDispatch-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI::Application) >= 4.0
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
%description
CGI::Application::Plugin::ActionDispatch adds attribute based support for
parsing the PATH_INFO of the incoming HTTP request. For those who are familiar
with Catalyst, the interface works very similar.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-ActionDispatch-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
