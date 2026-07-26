%global source0_hash eda4457dbbf81a4241b735a5d469d9727d8a3091d24af1ae3c9a20f024de51cc

Name:           perl-Catalyst-View-TT
Summary:        Template Toolkit View Class
Version:        0.46
Release:        10%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-View-TT-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-View-TT
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 5.70000
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Timer)
BuildRequires:  perl(Template::Provider::Encoding)
BuildRequires:  perl(Test::More)

Requires:       perl(Catalyst) >= 5.70000

%{?perl_default_filter}

%description
This is the Catalyst view base class for the Template Toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-View-TT-%{version}

find . -type f -exec chmod -x -c {} +

# silence rpmlint warnings
sed -i 's/\r//' t/lib/TestApp/Template/Any.pm

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README t/
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
