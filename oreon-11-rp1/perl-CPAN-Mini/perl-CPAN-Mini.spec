%global source0_hash f204293be26ac841acc87044a188db0f591e80881316c7a288aec0eece306155

Name:           perl-CPAN-Mini
Summary:        Create a minimal mirror of CPAN
Version:        1.111017
Release:        7%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Mini-%{version}.tar.gz 
URL:            https://metacpan.org/release/CPAN-Mini
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib) >= 1.20
# CPAN is optional and not used at tests
# CPANPLUS::Backend is optional and not used at tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir) >= 0.57
BuildRequires:  perl(File::Path) >= 2.04
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(LWP::UserAgent) >= 5
BuildRequires:  perl(Pod::Usage) >= 1.00
BuildRequires:  perl(URI) >= 1
# Tests:
BuildRequires:  perl(Test::More) >= 0.96

Suggests:       perl(CPAN)
Suggests:       perl(CPANPLUS::Backend)

Provides: minicpan = %{version}-%{release}

%{?perl_default_filter}

%description
CPAN::Mini provides a simple mechanism to build and update a minimal 
mirror of the CPAN on your local disk containing only those files 
needed to install the newest version of every distribution. 

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Mini-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t Changes %{buildroot}%{_libexecdir}/%{name}
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
%{_bindir}/minicpan
%{perl_vendorlib}/CPAN/Mini*
%{_mandir}/man1/minicpan*
%{_mandir}/man3/CPAN::Mini*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
