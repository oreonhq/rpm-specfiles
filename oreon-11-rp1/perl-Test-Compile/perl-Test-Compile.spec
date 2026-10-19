%global source0_hash df3ab30ecb51ae14a1aa9b9fc14324c969cc258ef2adacc35bc68194112da685
%global cpan_version v3.3.3
Name:           perl-Test-Compile
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        1%{?dist}
Summary:        Check whether Perl module files compile correctly
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Compile
Source0:        https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-%{cpan_version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_libexecdir}/%{name}/lib
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Compile lets you check the validity of a Perl module file or Perl script
file, and report its results in standard Test::Simple fashion.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Exception)
Requires:       perl(Test::Warnings)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Compile-%{cpan_version}

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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/lib/Test/Compile
for F in Test/Compile.pm Test/Compile/Internal.pm; do
    ln -s %{perl_vendorlib}/$F %{buildroot}%{_libexecdir}/%{name}/lib/$F
done
rm %{buildroot}%{_libexecdir}/%{name}/t/999-*
perl -i -ne 'print $_ unless m{\@INC = grep .* \@INC;}' %{buildroot}%{_libexecdir}/%{name}/t/scripts/messWithLib.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TEST
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Compile-tests -f %{oreon_filedir}/perl-Test-Compile-tests.list

%changelog

%autochangelog
