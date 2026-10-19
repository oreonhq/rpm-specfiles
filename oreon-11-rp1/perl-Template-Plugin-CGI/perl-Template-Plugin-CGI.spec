%global source0_hash e9b61e0f51c224706daadfa76ac21b926ed1bfb4ec853912167d8d9af1090570
Summary:        Simple Template Toolkit plugin interfacing to the CGI module
Name:          perl-Template-Plugin-CGI
Version:       3.101
Release:        1%{?dist}
License:       (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:           https://metacpan.org/release/Template-Plugin-CGI
Source0:        https://cpan.metacpan.org/modules/by-module/Template/Template-Plugin-CGI-%{version}.tar.gz
BuildArch:     noarch
Requires:      perl(CGI) >= 4.44
Conflicts:     perl-Template-Toolkit < 3.010-5
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Plugin)
BuildRequires:  perl(Template::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a very simple Template Toolkit Plugin interface to the CGI module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Template-Plugin-CGI-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_build pure_install DESTDIR=%{buildroot}
%oreon_autofiles main

%check

unset AUTHOR_TESTING
%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
