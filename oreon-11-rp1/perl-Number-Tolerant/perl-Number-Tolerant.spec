%global source0_hash fdd6b934ea034a4f61750f0e38dd66df7c565af1ed8891eef7c5ccde6047a3ce
Name:           perl-Number-Tolerant
Version:        1.710
Release:        9%{?dist}
Summary:        Tolerance ranges for inexact numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Number-Tolerant
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Number-Tolerant-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(overload)
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Sub::Exporter\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(base)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
These Perl modules create a number-like object whose value refers
to a range of possible values, each equally acceptable. It overloads
comparison operations to reflect this.

%package -n perl-Test-Tolerant
Summary:        Test routines for testing numbers against tolerances
Requires:       perl(Sub::Exporter) >= 0.950
%description -n perl-Test-Tolerant
"is_tol" is the only routine provided by Test::Tolerant Perl module. It
behaves like "is" from Test::More, asserting that two values must be equal,
but it will always use numeric equality, and the second argument is not always
used as the right hand side of comparison directly, but it used to produce
a Number::Tolerant to compare to.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Tolerant = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(feature)
Requires:       perl(Number::Tolerant::Union)
Requires:       perl(Test::More) >= 0.96
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Number-Tolerant-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Test-Tolerant usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Tolerant -f %{oreon_filedir}/perl-Test-Tolerant.list
%files -n perl-Number-Tolerant-tests -f %{oreon_filedir}/perl-Number-Tolerant-tests.list

%changelog

%autochangelog
