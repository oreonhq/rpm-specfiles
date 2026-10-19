%global source0_hash cffc0b960d783dfbcf7b247f5fea65c84de230ee2f091f142ca9b8aeb07e79d2
%global base_version 0.94
Name:           perl-Filter-Simple
Version:        0.96
Release:        521%{?dist}
Summary:        Simplified Perl source filtering
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Filter-Simple
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Filter-Simple-0.94.tar.gz
BuildArch:      noarch
Patch0:         Filter-Simple-0.94-Upgrade-to-0.95.patch
Patch1:         Filter-Simple-0.94-Upgrade-to-0.96.patch
Requires:       perl(Text::Balanced) >= 1.97
Requires:       perl(warnings)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::Balanced\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(Filter::Simple::.*\\)
Provides:       perl(Filter::Simple)
Provides:       perl(Filter::Simple)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Filter::Simple Perl module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Filter-Simple-%{base_version}
%patch -P0 -p1
%patch -P1 -p1

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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Filter-Simple-tests -f %{oreon_filedir}/perl-Filter-Simple-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.96-521
- Prepare for Oreon 11 (RP1)
