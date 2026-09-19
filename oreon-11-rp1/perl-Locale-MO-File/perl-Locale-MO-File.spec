%global source0_hash 97036dc3f09db37052ae9d9a514487e884b56d90c76ca12d6cab405d23564a3f

Name:           perl-Locale-MO-File
Version:        0.09
Release:        21%{?dist}
Summary:        Write and read gettext MO files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-MO-File
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Locale-MO-File-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-times
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)

BuildRequires:  perl(IO::File)
BuildRequires:  perl(Moo) >= 1.003001
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::HexDifferences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(utf8)
# Optional tests
BuildRequires:  perl(Pod::Coverage::Moose)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Moo) >= 1.003001

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Moo)\\)$

%description
The module allows to write or read gettext MO files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Locale-MO-File-%{version}
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
