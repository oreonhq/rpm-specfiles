%global source0_hash 100c27908757c56ebfeca8b7bf15a9867e449df663ff013de3855d183dfbea30
Name:           perl-Pod-Usage
Epoch:          4
Version:        2.05
Release:        521%{?dist}
Summary:        Print a usage message from embedded POD documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Usage
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Usage-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Spec) >= 0.82
Requires:       perl-Pod-Perldoc
Requires:       perl(Pod::Text) >= 4
%global __requires_exclude %{?__requires_exclude|%{__requires_exclude}|}^perl\\(File::Spec\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(Pod::Usage)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
pod2usage will print a usage message for the invoking script (using its
embedded POD documentation) and then exit the script with the desired exit
status. The usage message printed may have any one of three levels of
"verboseness": If the verbose level is 0, then only a synopsis is printed.
If the verbose level is 1, then the synopsis is printed along with a
description (if present) of the command line options and arguments. If the
verbose level is 2, then the entire manual page is printed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Pod::Text)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Usage-%{version}

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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{-Mblib}{}' %{buildroot}%{_libexecdir}/%{name}/t/pod/*
perl -i -pe 's{ \@blib,}{}' %{buildroot}%{_libexecdir}/%{name}/t/pod/pod2usage2.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/lib/Pod
mkdir -p %{buildroot}%{_libexecdir}/%{name}/scripts
ln -s %{perl_vendorlib}/Pod/Usage.pm %{buildroot}%{_libexecdir}/%{name}/lib/Pod/
ln -s %{_bindir}/pod2usage %{buildroot}%{_libexecdir}/%{name}/scripts/pod2usage.PL
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Pod-Usage-tests -f %{oreon_filedir}/perl-Pod-Usage-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4:2.05-521
- Import
