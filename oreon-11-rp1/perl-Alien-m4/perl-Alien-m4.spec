%global source0_hash ab2a405c803944fd01c51fa1e9f2befd5871ab03f1744dec2a56689f2148d361
%global debug_package %{nil}
Name:           perl-Alien-m4
Version:        0.21
Release:        11%{?dist}
Summary:        Find GNU m4
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-3.0-or-later
URL:            https://metacpan.org/dist/Alien-m4
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-m4-%{version}.tar.gz
Requires:       m4 %(perl -e 'print qq{ = $1} if qx{m4 --version} =~ m{(\d+\.\d+\.\d+)}' 2>/dev/null)
Requires:       perl(Alien::Base) >= 0.038
Requires:       perl(alienfile) >= 0.32
Requires:       perl(Capture::Tiny)
Requires:       perl(Config)
Requires:       perl(Path::Tiny)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base|Test2::V0|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build::MM)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package can be used by other Perl modules that require GNU m4.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000121
Requires:       perl(Test::More) >= 0.98
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-m4-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

unset M4
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset M4
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset M4
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-m4-tests -f %{oreon_filedir}/perl-Alien-m4-tests.list

%changelog

%autochangelog
