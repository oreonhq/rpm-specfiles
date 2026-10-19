%global source0_hash 2bea3209f18e273b193e3175a42d269391919e49ab106b6e252395d272182f65
%global base Text-Aspell
Name:		perl-%{base}
Version:	0.09
Release:        57%{?dist}
Summary:        Perl interface to the GNU Aspell library
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/%{base}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HANK/%{base}-%{version}.tar.gz
Requires:	aspell >= 0.50.1
%{?perl_default_filter}
# oreon:deps
BuildRequires:  aspell-devel
BuildRequires:  aspell-en
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a Perl interface to the GNU Aspell library.  This
module is to meet the need of looking up many words, one at a time, in a
single session, such as spell-checking a document in memory.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{base}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test TEST_POD=t
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
