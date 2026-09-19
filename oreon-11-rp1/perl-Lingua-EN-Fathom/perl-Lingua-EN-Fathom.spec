%global source0_hash db125587eb07542242d759ef02317ae76e82535c741d05e599c95fac275ccfe1

Name:           perl-Lingua-EN-Fathom
Version:        1.27
Release:        7%{?dist}
Summary:        Measure readability of English text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Fathom
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/Lingua-EN-Fathom-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Lingua::EN::Sentence) >= 0.28
BuildRequires:  perl(Lingua::EN::Syllable) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(Lingua::EN::Sentence) >= 0.28
Requires:       perl(Lingua::EN::Syllable) >= 0.28

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Lingua::EN::Syllable\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Lingua::EN::Sentence\\)$

%description
This module analyses English text in either a string or file. Totals are
then calculated for the number of characters, words, sentences, blank and
non blank (text) lines and paragraphs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Fathom-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes examples README
%{perl_vendorlib}/Lingua/EN/Fathom.pm
%{_mandir}/man3/Lingua::EN::Fathom.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
