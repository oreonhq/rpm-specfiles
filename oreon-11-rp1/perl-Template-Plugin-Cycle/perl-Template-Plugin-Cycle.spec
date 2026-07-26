%global source0_hash 6166656a41b3fad3d2b5154514379627a8b9ef3262117eb07420d8d55a83ab20

Name:           perl-Template-Plugin-Cycle
Version:        1.06
Release:        45%{?dist}
Summary:        Cyclically insert into a Template from a sequence of values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Plugin-Cycle
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Template-Plugin-Cycle-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.75
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util) >= 0.20
BuildRequires:  perl(Template) >= 2.10
BuildRequires:  perl(Template::Plugin)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(Params::Util) >= 0.20
Requires:       perl(Template) >= 2.10

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$

%description
Sometimes, apparently almost exclusively when doing alternating table row
backgrounds, you need to print an alternating, cycling, set of values into
a template.

Template::Plugin::Cycle is a small, simple, and hopefully DWIM solution to
these sorts of tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Plugin-Cycle-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
