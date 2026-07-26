%global source0_hash 5e870cb3f7e64f79fdfc8d984748dbc63b07ec188b0641d58cedd190dd9b29e0

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname HTML-Restrict

Summary:        Perl module to strip unwanted HTML tags and attributes
Name:           perl-HTML-Restrict
Version:        3.0.2
Release:        8%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{pkgname}-v%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.002000
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Type::Tiny) >= 1.002001
BuildRequires:  perl(Types::Standard) >= 1.000001
BuildRequires:  perl(URI)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod) >= 1.22 
BuildArch:      noarch

%description
A perl module that uses HTML::Parser to strip HTML from text in a
restrictive manner. By default all HTML is restricted, but default
behaviour may be altered by supplying own tag rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

# Don't add dependencies for %%doc
chmod -x examples/*
sed -i -e '1s|#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|' examples/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README.md examples
%{perl_vendorlib}/HTML/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
