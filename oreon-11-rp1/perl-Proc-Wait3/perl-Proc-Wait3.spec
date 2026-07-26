%global source0_hash 1a907f5db6933dc2939bbfeffe19eeae7ed39ef1b97a2bc9b723f2f25f81caf3

Name:           perl-Proc-Wait3
Version:        0.05
Release:        36%{?dist}
Summary:        Perl extension for wait3 system call
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-Wait3
Source0:        https://cpan.metacpan.org/authors/id/C/CT/CTILMES/Proc-Wait3-%{version}.tar.gz

BuildRequires:  %{__make}
BuildRequires:  gcc
BuildRequires:  %{__perl}
BuildRequires:  /usr/bin/iconv

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)

%description
If any child processes have exited, this call will "reap" the zombies
similar to the perl "wait" function.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-Wait3-%{version}
/usr/bin/iconv -f ISO-8859-1 -t utf-8 < Changes > Changes~
mv Changes~ Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Proc*
%{_mandir}/man3/*

%changelog
%autochangelog
