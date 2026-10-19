%global source0_hash 3b309ec091d099cdc1a1abac5e00ec5787f3426241503449658d5ea91dff871e
Name:           perl-perlindex
Version:        1.606
Release:        36%{?dist}
Summary:        Index and search the perl documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/perlindex
Source0:        https://cpan.metacpan.org/authors/id/U/UL/ULPFR/perlindex-%{version}.tar.gz
Patch0:         perlindex-1.606-Remove-useless-interpreter-declaration-from-Text-Eng.patch
Patch1:         perlindex-1.606-Allow-testing-installed-code.patch
BuildArch:      noarch
Requires:       perl(File::Find)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test)
BuildRequires:  perl(blib)
BuildRequires:  perl(less)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perlindex is a program to index and search the perl documentation. It provides
Text::English module implementing Porter stemming algorithm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n perlindex-%{version}
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a MANIFEST perlindex.PL README t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-perlindex-tests -f %{oreon_filedir}/perl-perlindex-tests.list

%changelog

%autochangelog
