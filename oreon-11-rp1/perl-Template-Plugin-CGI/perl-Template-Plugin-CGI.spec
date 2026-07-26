%global source0_hash e9b61e0f51c224706daadfa76ac21b926ed1bfb4ec853912167d8d9af1090570

Summary:       Simple Template Toolkit plugin interfacing to the CGI module
Name:          perl-Template-Plugin-CGI
Version:       3.101
Release:       11%{?dist}
License:       (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:           https://metacpan.org/release/Template-Plugin-CGI
Source:        https://cpan.metacpan.org/modules/by-module/Template/Template-Plugin-CGI-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: make
BuildRequires: perl(base)
BuildRequires: perl(blib)
BuildRequires: perl(CGI) >= 4.44
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Spec)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(Template) >= 3.100
BuildRequires: perl(Template::Plugin)
BuildRequires: perl(Template::Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(warnings)

Requires:      perl(CGI) >= 4.44
Conflicts:     perl-Template-Toolkit < 3.010-5

%{?perl_default_filter}

%description
This is a very simple Template Toolkit Plugin interface to the CGI module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Template-Plugin-CGI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}

%check
unset AUTHOR_TESTING
%make_build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/Template::Plugin::CGI*3pm*

%changelog
%autochangelog
