%global source0_hash d735febf9464fb9e0b1a5a803ba835db7ac71454340e9bc1af6d1fc86e8b4003

Name:           perl-Math-Symbolic
Version:        0.613
Release:        4%{?dist}
Summary:        Symbolic calculations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Symbolic
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Math-Symbolic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Memoize) >= 1.01
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Memoize) >= 1.01

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Memoize\\)$

%description
Math::Symbolic is intended to offer symbolic calculation capabilities to
the Perl programmer without using external (and commercial) libraries
and/or applications.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Symbolic-%{version}
for file in Changes README `find lib -name '*.pm'`; do
  iconv -flatin1 -tutf8 < $file > $file.utf8
  touch -r $file $file.utf8
  mv $file.utf8 $file
done
chmod -c a-x examples/*

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
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
./Build test

%files
%doc Changes README TODO Yapp.yp examples
%dir %{perl_vendorlib}/Math
%{perl_vendorlib}/Math/Symbolic*
%{_mandir}/man3/Math::Symbolic*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
