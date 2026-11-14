# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 36cf8c16ec969826217ff7458535a29714cb471dadba1672a303034d029a6e64
%global vsp_version 0.001
%global source1_hash 0fff1f02c61b7098a6d2eb9698a052cf00b87becf2705d2d1f0d395f8d87a7e3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           perl-generators
Version:        1.16
Release:        1%{?dist}
Summary:        RPM Perl dependencies generators
License:        GPL-1.0-or-later
URL:            http://jplesnik.fedorapeople.org/generators
Source0:        http://jplesnik.fedorapeople.org/generators/generators-%{version}.tar.gz
Source1:        https://ppisar.fedorapeople.org/Fedora-VSP/Fedora-VSP-%{vsp_version}.tar.gz
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
BuildRequires:  perl(File::Basename)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  oreon-rpm-macros
Requires:       perl-interpreter >= 4:5.22.0-351
# Per Perl packaging guidelines, build-requiring perl-generators should
# deliver Perl macros
Requires:       perl-macros
Requires:       perl(Oreon::VSP)
Requires:       perl(File::Basename)
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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -

%setup -q -n generators-%{version}
sed -i \
    -e 's|Fedora::VSP|Oreon::VSP|g' \
    -e 's|Fedora-VSP|Oreon-VSP|g' \
    template/bin/perl.req Makefile.PL META.yml META.json
mkdir -p _oreon_vsp/Oreon
tar -xOf %{SOURCE1} Fedora-VSP-%{vsp_version}/lib/Fedora/VSP.pm \
    | sed 's/Fedora::VSP/Oreon::VSP/g' > _oreon_vsp/Oreon/VSP.pm
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
export PERL5LIB="$PWD/_oreon_vsp${PERL5LIB:+:$PERL5LIB}"
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
export PERL5LIB="$PWD/_oreon_vsp${PERL5LIB:+:$PERL5LIB}"
make test

%files
%doc Changes TODO
%{_rpmconfigdir}/perl*
%{_rpmconfigdir}/fileattrs/perl*.attr

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
