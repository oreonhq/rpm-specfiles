%global source0_hash fb2bf94ed8dbc1f4a95d9fc8f710cb67b3f796c6efc9c4bb4c2cfa3ebaa1c5fa

Name:		perl-Regexp-Trie
Version:	0.02
Release:	22%{?dist}
Summary:	Build trie-ized regexp
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Regexp-Trie
Source0:	https://cpan.metacpan.org/modules/by-module/Regexp/Regexp-Trie-%{version}.tar.gz
Patch0:		Regexp-Trie-0.02-test.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	procps-ng
BuildRequires:	words
# Dependencies
# (none)

Provides:       perl(Regexp::Trie)
%description
This module is a faster but simpler version of Regexp::Assemble or
Regexp::Optimizer. It builds a trie-ized regexp as above. This module is
faster than Regexp::Assemble but you can only add literals:
a+b is treated as a\+b, not "more than one a's followed by b".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Regexp-Trie-%{version}

# Fix issues in t/01-dict.t
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
prove --lib %{buildroot}%{perl_vendorlib} t/01-dict.t :: /usr/share/dict/words

%files
%doc Changes README
%{perl_vendorlib}/Regexp/
%{_mandir}/man3/Regexp::Trie.3*

%changelog
%autochangelog
