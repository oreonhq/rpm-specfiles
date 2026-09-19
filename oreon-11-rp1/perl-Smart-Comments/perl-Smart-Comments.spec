%global source0_hash dcf8a312134a7c6b82926a0115d93b692472a662d28cdc3a9bdf28984ada9ee3

Name:           perl-Smart-Comments
Summary:        Comments that do more than just sit there
Epoch:          1
Version:        1.06
Release:        29%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Smart-Comments-%{version}.tar.gz
URL:            https://metacpan.org/release/Smart-Comments
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Simple) >= 0.8
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.99
BuildRequires:  perl(Text::Balanced) >= 2
BuildRequires:  perl(warnings)

# Drop the old tests subpackage
# Can be removed diromg F22 development cycle
Obsoletes:      %{name}-tests < 1:1.000004-1
Provides:       %{name}-tests = %{epoch}:%{version}-%{release}

%{?perl_default_filter}

%description
Smart comments provide an easy way to insert debugging and tracking code into
a program. They can report the value of a variable, track the progress of a
loop, and verify that particular assertions are true.

Best of all, when you're finished debugging, you don't have to remove them.
Simply commenting out the use Smart::Comments line turns them back into
regular comments. Leaving smart comments in your code is smart because if you
needed them once, you'll almost certainly need them again later.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Smart-Comments-%{version}
perl -pi -e 's|^#!perl -T|#!%{_perl}|' t/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
