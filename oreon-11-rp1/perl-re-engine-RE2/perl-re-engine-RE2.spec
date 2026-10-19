%global source0_hash b317fd54e25d1c67e41f84725d232f3688cdea4ab686e6095984f6fc932c5fa1
Name:           perl-re-engine-RE2
Summary:        RE2 regex engine
Version:        0.18
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND dtoa
URL:            https://metacpan.org/release/re-engine-RE2
Source0:        https://cpan.metacpan.org/authors/id/D/DG/DGL/re-engine-RE2-%{version}.tar.gz
Patch0:         re-engine-RE2-0.18-Unbundle-re2.patch
Patch1:         re-engine-RE2-0.18-Use-C-17.patch
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:    %{ix86}
%endif
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  re2-devel
# /oreon:deps
%description
This module replaces perl's regex engine in a given lexical scope with RE2.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n re-engine-RE2-%{version}
# Remove bundled code, MANIFEST is correct with a patch
rm -r ./re2
# Remove incorrect executable bits
chmod -x lib/re/engine/RE2.pm
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-re-engine-RE2-tests -f %{oreon_filedir}/perl-re-engine-RE2-tests.list

%changelog

%autochangelog
