%global source0_hash 08236a913b911ce652cf08598e7c07d2df3f369fc47bf401a485a504a1660783

Name:           perl-String-Formatter
Version:        1.235
Release:        9%{?dist}
Summary:        Build sprintf-like functions of your own
License:        GPL-2.0-only
URL:            https://metacpan.org/release/String-Formatter
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/String-Formatter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Sub::Exporter)
# tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96

%{?perl_default_filter}

%description
String::Formatter is a tool for building sprintf-like formatting routines.
It supports named or positional formatting, custom conversions, fixed
string interpolation, and simple width-matching out of the box. It is easy
to alter its behavior to write new kinds of format string expanders. For
most cases, it should be easy to build all sorts of formatters out of the
options built into String::Formatter.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Formatter-%{version}
perl -MConfig -pi -e 's|^#!.*perl\b|$Config{startperl}|' misc/bench.pl

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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README misc/bench.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
