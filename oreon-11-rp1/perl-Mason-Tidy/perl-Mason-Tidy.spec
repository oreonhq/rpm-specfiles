%global source0_hash 58bedd46a43e17190d22ce6cdd9626b990017a8f0ee326807b54cf5c92f85d7a

Name:           perl-Mason-Tidy
Version:        2.57
Release:        31%{?dist}
Summary:        Tidy HTML::Mason/Mason components
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mason-Tidy
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSWARTZ/Mason-Tidy-%{version}.tar.gz
# Adapt to changes in Perl-Tidy-20180219, bug #1549515, CPAN RT#124604
Patch0:         Mason-Tidy-2.57-Adapt-to-changes-in-Perl-Tidy-20180219.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
# IPC::Run3 not required for tests
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Method::Signatures::Simple) >= 1.02
BuildRequires:  perl(Moo) >= 0.0091010
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Class::Most)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Method::Signatures::Simple) >= 1.02
Requires:       perl(Moo) >= 0.0091010

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Method::Signatures::Simple\\)\\s*$

Provides:       perl(Mason::Tidy)
%description
Mason::Tidy is the engine used by masontidy. You can call this API from
your own program instead of executing masontidy.

masontidy tidies Mason 1 and Mason 2 components, using perltidy to format
the Perl code that can be embedded in various places in the component.
masontidy does not (yet) attempt to tidy the HTML or other non-Perl content
in a component.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mason-Tidy-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/masontidy
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/Mason/Tidy/t

%changelog
%autochangelog
