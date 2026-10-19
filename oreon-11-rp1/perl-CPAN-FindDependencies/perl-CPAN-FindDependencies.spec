%global source0_hash 13b057a77399bbde46f752f7b745326a62aa39fab2eda755ce441e0185e5a50f
%global pkgname CPAN-FindDependencies
%bcond_with perl_CPAN_FindDependencies_enables_network
%bcond_without perl_CPAN_FindDependencies_enables_optional_test
Name:           perl-CPAN-FindDependencies
Version:        3.13
Release:        1%{?dist}
Summary:        Find dependencies for modules on CPAN
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-FindDependencies
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_CPAN_FindDependencies_enables_network}
%endif
%if %{with perl_CPAN_FindDependencies_enables_optional_test}
%endif
Requires:       bzip2
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Pod::Perldoc)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(.::t/.*\\)
# oreon:deps
BuildRequires:  bzip2
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::CheckOS)
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Parse::CPAN::Packages)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Time)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides tools to find a module's dependencies (and their
dependencies, and so on) without having to download the modules in
their entirety.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}
for F in \
%if !%{with perl_CPAN_FindDependencies_enables_network}
    t/cpandeps-diff-script.t \
%endif
%if !%{with perl_CPAN_FindDependencies_enables_optional_test}
    t/pod.t t/pod-coverage.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t t/cache/Tie-Scalar-Decay-1.1.1/Tie-Scalar-Decay-1.1.1.MakefilePL; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod{,-coverage}.t
mkdir %{buildroot}%{_libexecdir}/%{name}/blib
ln -s %{_bindir} %{buildroot}%{_libexecdir}/%{name}/blib/script
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
chmod 0755 "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-CPAN-FindDependencies-tests -f %{oreon_filedir}/perl-CPAN-FindDependencies-tests.list

%changelog

%autochangelog
