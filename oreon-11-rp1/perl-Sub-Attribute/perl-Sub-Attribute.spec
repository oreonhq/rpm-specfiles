%global source0_hash 6f0e3d494d77132b26ef3908a569e9b78797df6c22be82c202b4d171225b8f26

Name:           perl-Sub-Attribute
Version:        0.07
Release:        23%{?dist}
Summary:        Reliable subroutine attribute handlers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Attribute/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Sub-Attribute-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(attributes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Trigger) >= 0.14
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
# Optional tests
# Test::Pod 1.14
# Test::Pod::Coverage 1.04
# Test::Synopsis
Requires:       perl(parent) >= 0.221

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(parent\\)$

%description
Sub::Attribute is a role to define attribute handlers for specific
subroutine attributes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sub-Attribute-%{version}
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' example/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test SUB_ATTRIBUTE_DEBUG=0

%files
%doc CHANGELOG example README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sub*
%{_mandir}/man3/*

%changelog
%autochangelog
