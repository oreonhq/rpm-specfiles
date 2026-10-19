%global source0_hash 3f83a451fcf9492a26847f8694c7384a69b032088f785ba9c2536b94c7d61d50
Name:           perl-Perl-Tidy-Sweetened
Version:        1.20
Release:        1%{?dist}
Summary:        Tweaks to Perl::Tidy to support some syntactic sugar
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Tidy-Sweetened
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRIMES/Perl-Tidy-Sweetened-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Tidy) >= 20230309
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Tidy\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(TidierTests\\)
Provides:       perl(Perl::Tidy::Sweetened)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
There are a number of modules on CPAN that allow users to write their
classes with a more "modern" syntax. These tools eliminate the need to
shift off $self, can support type checking and offer other improvements.
Unfortunately, they can break the support tools that the Perl community has
come to rely on. This module attempts to work around those issues.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-Tidy-Sweetened-%{version}

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Perl-Tidy-Sweetened-tests -f %{oreon_filedir}/perl-Perl-Tidy-Sweetened-tests.list

%changelog

%autochangelog
