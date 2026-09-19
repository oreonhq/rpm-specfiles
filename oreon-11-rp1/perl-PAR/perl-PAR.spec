%global source0_hash 732fcfd3c1ba8bb314d7df92d14209e066d19b4c45f8451e58d684f0ddfe6bf3

Name:           perl-PAR
Version:        1.021
Release:        2%{?dist}
Summary:        Perl Archive Toolkit
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PAR
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/PAR-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl(Archive::Unzip::Burst)
BuildRequires:  perl(Archive::Zip) >= 1
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
# XXX: BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA) >= 5.45
# XXX: BuildRequires:  perl(Digest::SHA1)
# XXX: BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Fcntl)
# XXX: BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.05
# XXX: BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(AutoLoader) >= 5.66
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(Archive::Zip) >= 1
Requires:       perl(Digest::SHA) >= 5.45
Requires:       perl(File::Glob)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp) >= 0.05
Requires:       perl(LWP::Simple)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Zip\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(Data\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Hello\\)

%description
This module lets you use special zip files, called Perl Archives, as
libraries from which Perl modules can be loaded.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PAR-%{version}

# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl`; do
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
perl -i -pe 's{-Mblib }{}' %{buildroot}%{_libexecdir}/%{name}/t/01-basic.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_TEST_POD
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_TEST_POD
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc AUTHORS Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
