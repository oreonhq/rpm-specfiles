Name:           perl-Getopt-Long
Epoch:          1
Version:        2.58
Release:        521%{?dist}
Summary:        Extended processing of command line options
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Getopt-Long
Source0:        https://cpan.metacpan.org/authors/id/J/JV/JV/Getopt-Long-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 1305ed46ea21f794304e97aa3dcd3a38519059785e9db7415daf2c218506c569
%global source0_file Getopt-Long-2.58.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Text::ParseWords)
# Recommended:
Requires:       perl(Pod::Usage) >= 1.14
# Dependencies on these Perl 4 files are generated as perl(foo.pl):
Provides:       perl(newgetopt.pl) = %{version}

%description
The Getopt::Long module implements an extended getopt function called
GetOptions(). It parses the command line from @ARGV, recognizing and removing
specified options and their possible values.  It adheres to the POSIX syntax
for command line options, with GNU extensions. In general, this means that
options have long names instead of single letters, and are introduced with
a double dash "--". Support for bundling of command line options, as was the
case with the more traditional single-letter approach, is provided but not
enabled by default.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(newgetopt.pl)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Getopt-Long-2.58.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1305ed46ea21f794304e97aa3dcd3a38519059785e9db7415daf2c218506c569" || { echo "oreon: Source0 SHA256 mismatch for Getopt-Long-2.58.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Getopt-Long-%{version}

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
%doc Changes examples README.md
%dir %{perl_vendorlib}/Getopt
%{perl_vendorlib}/Getopt/Long*
%{perl_vendorlib}/newgetopt.pl*
%{_mandir}/man3/Getopt::Long*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.58-521
- Prepare for Oreon 11 (RP1)
