%global source0_hash 36cf8c16ec969826217ff7458535a29714cb471dadba1672a303034d029a6e64

Name:           perl-generators
Version:        1.16
Release:        9%{?dist}
Summary:        RPM Perl dependencies generators
License:        GPL-1.0-or-later
URL:            http://jplesnik.fedorapeople.org/generators
Source0:        http://jplesnik.fedorapeople.org/generators/generators-1.16.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
%if !%{defined perl_bootstrap}
# Break build cycle: reflexive dependency
BuildRequires:  perl-generators
%endif
BuildRequires:  perl-interpreter >= 4:5.22.0-351
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Fedora::VSP)
BuildRequires:  perl(File::Basename)
# Optional run-time:
# version not used at tests
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
Requires:       perl-interpreter >= 4:5.22.0-351
# Per Perl packaging guidelines, build-requiring perl-generators should
# deliver Perl macros
Requires:       perl-macros
%if %{defined perl_bootstrap}
# Supply run-time dependencies manually when perl-generators is not available
Requires:       perl(Fedora::VSP)
Requires:       perl(File::Basename)
%endif
Recommends:     perl(version)

# The generators and attribute files were split from rpm-build
Conflicts:      rpm-build < 4.11.2-15

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PerlNS\\)

%description
This package provides RPM Perl dependencies generators which are used for
getting provides and requires from Perl binaries and modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{defined perl_bootstrap}
# Supply run-time dependencies manually when perl-generators is not available
Requires:       perl(Exporter)
Requires:       perl(lib)
Requires:       perl(strict)
Requires:       perl(Test::More)
Requires:       perl(Test::Simple)
Requires:       perl(warnings)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n generators-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor INSTALLVENDORSCRIPT=%{_rpmconfigdir} \
     NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs/
install -p -m 644 fileattrs/* '%{buildroot}%{_rpmconfigdir}/fileattrs'

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe "s{bin/perl}{%{_rpmconfigdir}/perl}" %{buildroot}%{_libexecdir}/%{name}/t/lib/PerlNS.pm
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes TODO
%{_rpmconfigdir}/perl*
%{_rpmconfigdir}/fileattrs/perl*.attr

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-9
- Prepare for Oreon 11 (RP1)
