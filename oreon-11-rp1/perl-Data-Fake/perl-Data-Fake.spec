%global source0_hash 930960e04a417fb19e14ce1e739e3e4aefbddd101eae68bfa25ba7674fe7c2a1

Name:           perl-Data-Fake
Version:        0.006
Release:        5%{?dist}
Summary:        Declaratively generate fake structured data for testing
License:        Apache-2.0
URL:            https://metacpan.org/release/Data-Fake
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Data-Fake-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Import::Into) >= 1.002005
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Text::Lorem)
BuildRequires:  perl(Time::Piece) >= 1.27
# Test
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Text::Lorem)

%description
This module generates randomized, fake structured data using
declarative syntax.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Fake-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/Data/Fake*
%{_mandir}/man3/Data::Fake*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
