%global source0_hash a63945ecdd420afc311094f93a220cfb35df23242de619e53ba67477a13690a2

Name:           perl-Test-HexDifferences
Version:        1.001
Release:        25%{?dist}
Summary:        Test binary as hexadecimal string
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HexDifferences
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Test-HexDifferences-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Builder::Module) >= 0.99
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Tester)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Test::Builder::Module) >= 0.99

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Test::Builder::Module)\\)$

%description
This is a Perl module for testing equivalence of binary data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-HexDifferences-%{version}
sed -i -e 's/\r//' README Changes example/*
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' example/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes example README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
