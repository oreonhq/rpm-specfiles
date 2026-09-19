%global source0_hash b518f367a8ad6486118f9283c4bb9b6c6f818c4ee334402dda6b6c941925e871

Name:           perl-Data-Dmp
Version:        0.242
Release:        9%{?dist}
Summary:        Dump Perl data structures as Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Dmp
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Data-Dmp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Regexp::Stringify)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(B::Deparse)
Requires:       perl(Regexp::Stringify)

%description
This module is a Perl dumper like Data::Dumper. It's compact, starts fast
and does not use any non-core modules except Regexp::Stringify when dumping
regexes. It produces compact single-line output (similar to
Data::Dumper::Concise). It supports dumping objects, regexes, circular
structures, coderefs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Dmp-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
chmod a-x devscripts/bench
perl -MConfig -i -pe 's|^#!.*perl\b|$Config{startperl}|' devscripts/bench

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author-*.t
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
%doc Changes devscripts README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
