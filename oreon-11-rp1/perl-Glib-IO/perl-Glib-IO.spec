%global source0_hash f40facf4d4b2e5125dbebde51b5e4ed35f8394bc43316ca7be743b9bb70f7443
Name:           perl-Glib-IO
Version:        0.002
Release:        1%{?dist}
Summary:        Perl bindings to the GIO library
License:        LGPL-2.1-only
URL:            http://metacpan.org/release/Glib-IO
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-IO-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Glib::Object::Introspection) >= 0.014
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Glib::Object::Introspection\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Glib::IO module allows a Perl developer to access the GIO library, the
high level I/O and platform library of the GNOME development platform.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Glib-IO-%{version}
# Help generators to recognize a Perl code
for F in t/*; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Glib-IO-tests -f %{oreon_filedir}/perl-Glib-IO-tests.list

%changelog

%autochangelog
