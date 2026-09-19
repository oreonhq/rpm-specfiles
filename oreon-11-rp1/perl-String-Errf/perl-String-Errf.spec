%global source0_hash e1fedbf9b4fd64b64ea81038ddb76a4c6cd85f5db15bc21f10656a298349dc1f

Name:           perl-String-Errf
Version:        0.009
Release:        9%{?dist}
Summary:        Simple sprintf-like dialect
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Errf
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/String-Errf-%{version}.tar.gz
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
BuildRequires:  perl(Carp)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Formatter) >= 0.102081
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Time::Piece)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Test::More) >= 0.96

%{?perl_default_filter}

%description
String::Errf provides errf, a simple string formatter that works something
like sprintf. It is implemented using String::Formatter and Sub::Exporter.
Their documentation may be useful in understanding or extending
String::Errf.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Errf-%{version}

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
%{_fixperms} $RPM_BUILD_ROOT/*

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
