%global source0_hash fcaba168aa05f1d4c65d213e3733abacb4d480ab4174e79860e12e3bfb2ecb14

Name:           perl-TeX-Hyphen
Version:        1.18
Release:        27%{?dist}
Summary:        Hyphenate words using TeX's patterns
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.adelton.com/perl/TeX-Hyphen/
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JANPAZ/TeX-Hyphen-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Benchmark)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TeX-Hyphen-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/TeX/
%{_mandir}/man3/TeX::Hyphen.3*
%{_mandir}/man3/TeX::Hyphen::czech.3*
%{_mandir}/man3/TeX::Hyphen::german.3*
%{_mandir}/man3/TeX::Hyphen::utf8.3*

%changelog
%autochangelog
