%global source0_hash 02f5afe2b4386e09b6cb3a39b5a102b74e789a3e29722994a20a8e3285c561c7
Name:           perl-UUID
Version:        0.37
Release:        1%{?dist}
Summary:        Universally Unique Identifier library for Perl
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/UUID
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRM/UUID-%{version}.tar.gz
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Temp|Test::More)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(MyNote\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MyNote\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The UUID library is used to generate unique identifiers for objects that may
be accessible beyond the local system. The generated UUIDs are compatible with
those created by the Open Software Foundation (OSF) Distributed Computing
Environment (DCE).

All generated UUIDs are either version 1, 3, 4, 5, 6, or version 7. And all
are variant 1, meaning compliant with the OSF DCE standard as described in
RFC 4122. Versions 6 and 7 are not standardized. They are presented here as
proposed in RFC 4122bis, version 14, and may change in the future.

%package tests
Summary:        Tests for %{name}
License:        Artistic-2.0
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Digest::SHA1)
Requires:       perl(File::Temp) >= 0.10
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n UUID-%{version}
# Remove always skipped tests
for T in t/0gen.t t/5persist/symlink.t t/9benchmark/*.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done

%build

unset AUTOMATED_TESTING NONINTERACTIVE_TESTING PERL_CPAN_REPORTER_CONFIG
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -r -I t/0LIB -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-UUID-tests -f %{oreon_filedir}/perl-UUID-tests.list

%changelog

%autochangelog
