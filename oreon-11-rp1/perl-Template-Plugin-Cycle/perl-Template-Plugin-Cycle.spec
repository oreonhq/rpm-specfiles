%global source0_hash 6166656a41b3fad3d2b5154514379627a8b9ef3262117eb07420d8d55a83ab20
Name:           perl-Template-Plugin-Cycle
Version:        1.06
Release:        1%{?dist}
Summary:        Cyclically insert into a Template from a sequence of values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Plugin-Cycle
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Template-Plugin-Cycle-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Params::Util) >= 0.20
Requires:       perl(Template) >= 2.10
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Plugin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
