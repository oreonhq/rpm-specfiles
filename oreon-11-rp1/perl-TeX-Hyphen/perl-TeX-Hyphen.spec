%global source0_hash fcaba168aa05f1d4c65d213e3733abacb4d480ab4174e79860e12e3bfb2ecb14
Name:           perl-TeX-Hyphen
Version:        1.18
Release:        1%{?dist}
Summary:        Hyphenate words using TeX's patterns
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.adelton.com/perl/TeX-Hyphen/
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JANPAZ/TeX-Hyphen-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
