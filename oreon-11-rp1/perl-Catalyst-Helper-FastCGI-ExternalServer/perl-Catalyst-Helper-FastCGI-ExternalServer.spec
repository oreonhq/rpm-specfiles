%global source0_hash 8cdf645a33088535c365a4e009b5fd7f7fbb927420a779a390f9fe92374121ad
Name:       perl-Catalyst-Helper-FastCGI-ExternalServer 
Version:    0.05 
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:        FastCGI daemon start/stop script for using FastCgiExternalServer
Source0:        https://cpan.metacpan.org/authors/id/Z/ZI/ZIGOROU/Catalyst-Helper-FastCGI-ExternalServer-%{version}.tar.gz
Url:        https://metacpan.org/release/Catalyst-Helper-FastCGI-ExternalServer
BuildArch:  noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(FCGI::ProcManager)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::TestBase)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module allows configuration using /etc/sysconfig/myapp. First make
a file called /etc/sysconfig/myapp and then write some variables in it.
The variables that you add to the file will automatically override the
environment variables.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Helper-FastCGI-ExternalServer-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
