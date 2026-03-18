Summary:        Tools to test taintedness
Name:           perl-Test-Taint
Version:        1.08
Release:        23%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Taint
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Test-Taint-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)


%{?perl_default_filter}

%description
Tainted data is data that comes from an unsafe source, such as the command
line, or, in the case of web apps, any GET or POST transactions. Read the 
perlsec man page for details on why tainted data is bad, and how to untaint
the data.

When you're writing unit tests for code that deals with tainted data, you'll
want to have a way to provide tainted data for your routines to handle, and 
easy ways to check and report on the taintedness of your data, in standard 
Test::More style.

%prep
%setup -q -n Test-Taint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="${RPM_OPT_FLAGS}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorarch}/Test
%{perl_vendorarch}/auto/Test
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.08-23
- Prepare for Oreon 11 (RP1)
