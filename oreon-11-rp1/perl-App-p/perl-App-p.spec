%global source0_hash 22107800ee8f1444238bdcfb3b4fe2f25d04e1d88b3ac2a5870cd345315f4456

Name:           perl-App-p
Version:        0.0400
Release:        30%{?dist}
Summary:        Steroids for your perl one-liners
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-p
Source0:        https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/App-p-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Modules are autoloaded by L module that is loaded by '-ML' exec's argument
Requires:       perl(Data::Dump)
Requires:       perl(Encode)
Requires:       perl(File::Slurper)
Requires:       perl(JSON)
Requires:       perl(L)
Requires:       perl(List::AllUtils)
Requires:       perl(LWP::Simple)
Requires:       perl(utf8::all)
Requires:       perl(XML::Hash::LX)
Requires:       perl(XML::Simple)
Requires:       perl(YAML)

%description
Provided tool "p" allows you to write and run perl one-liners in even more
compact syntax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-p-%{version}
sed -i -e '1 s|^#!.*|%(perl -MConfig -e 'print $Config{startperl}')|' bin/p

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
