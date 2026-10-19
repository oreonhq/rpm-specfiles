%global source0_hash 362bcf3500afd488e2aec137ca07ebdce7b5469d59c5337f9e778ed356af9ef1
Name:           perl-Class-Exporter
Version:        0.03
Release:        47%{?dist}
Summary:        Export class methods as regular subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Exporter
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Exporter-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module makes it much easier to make a module have a hybrid
object/method interface similar to the one of CGI.pm. You can take any
old module that has an object- oriented interface and convert it to
have a hybrid interface by simply adding "use base 'Class::Exporter'"
to your code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Exporter-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
chmod a-x README  blib/lib/Class/Exporter.pm
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
