%global source0_hash f13516d572941f68a1c23f2e0e49f5bf09b22f907eb9292b72baffe627bbee3c

Name:           perl-capitalization
Version:        0.03
Release:        53%{?dist}
Summary:        No capitalization on method names

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/capitalization
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/capitalization-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:	perl(Test::More)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n capitalization-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
