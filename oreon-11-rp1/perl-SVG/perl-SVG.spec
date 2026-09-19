%global source0_hash 74751f6880accbf93b2235161ec459a3d07909928794c90f1adc91b158db7711

Name:           perl-SVG
Version:        2.89
Release:        1%{?dist}
Summary:        An extension to generate stand-alone or inline SGV
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVG
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/SVG-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test::More) >= 0.94

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(SVG::Element\\)$

%description
SVG.pm is a Perl extension to generate stand-alone or inline SVG
(scaleable vector graphics) images using the W3C SVG XML recommendation

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVG-%{version}

# avoid extra dependencies
chmod 644 examples/*

# Fix line-endings
for i in SVG_02_sample.pl image_sample.pl inline_sample.pl inlinesvg.pl starpath.cgi sun_text_sample.pl svgtest2.pl ; do
    perl -pi -e 's/\r//' examples/$i
done

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

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
%doc README Changes examples
%{perl_vendorlib}/SVG*
%{_mandir}/man3/SVG*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
