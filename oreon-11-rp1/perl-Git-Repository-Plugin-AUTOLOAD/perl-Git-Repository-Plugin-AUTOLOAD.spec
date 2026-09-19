%global source0_hash 0dd39bd319651a81c3a9f514db78922f960d14bf3842665dd3312869b7a608b2

Name:           perl-Git-Repository-Plugin-AUTOLOAD
Version:        1.003
Release:        30%{?dist}
Summary:        Git subcommands as Git::Repository methods
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Git-Repository-Plugin-AUTOLOAD
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/Git-Repository-Plugin-AUTOLOAD-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Git::Repository::Plugin)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Repository) >= 1.309
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Git)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires::Git) >= 1.005
# Optional tests only
# CPAN::Meta not useful
# CPAN::Meta::Prereqs not useful

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Requires::Git\\)$

%description
This module adds an AUTOLOAD method to Git::Repository, enabling it to
automagically call git commands as methods on Git::Repository objects.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(lib)
Requires:       perl(Test::Requires::Git) >= 1.005

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Git-Repository-Plugin-AUTOLOAD-%{version}
# Remove always skipped tests
for T in t/author-pod-coverage.t t/author-pod-syntax.t t/release-distmeta.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E}' MANIFEST
done
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Git
%dir %{perl_vendorlib}/Git/Repository
%dir %{perl_vendorlib}/Git/Repository/Plugin
%{perl_vendorlib}/Git/Repository/Plugin/AUTOLOAD.pm
%{_mandir}/man3/Git::Repository::Plugin::AUTOLOAD.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
