%global source0_hash 7bc6242d746378982a599b34de35f07d3decc9e09d5646f8fa3b87f459414a4a

# Run optional test
%if ! (0%{?rhel})
%{bcond_without perl_Syntax_Keyword_Try_enables_extra_tests}
%else
%{bcond_with perl_Syntax_Keyword_Try_enables_extra_tests}
%endif

Name:           perl-Syntax-Keyword-Try
Version:        0.31
Release:        2%{?dist}
Summary:        try/catch/finally syntax for perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Try/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Try-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(XS::Parse::Keyword::Builder) >= 0.35
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(XS::Parse::Keyword) >= 0.35
# Tests
BuildRequires:  perl(overload)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::V0)
# Optional
%if %{with perl_Syntax_Keyword_Try_enables_extra_tests}
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Syntax::Keyword::Defer)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
BuildRequires:  perl(threads)

Requires:       perl(XS::Parse::Keyword) >= 0.35

Provides:       perl(Syntax::Keyword::Try)
Provides:       perl(Syntax::Keyword::Try)
%description
This module provides a syntax plugin that implements exception-handling
semantics in a form familiar to users of other languages, being built on a
block labeled with the try keyword, followed by at least one of a catch or
finally block.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Syntax_Keyword_Try_enables_extra_tests}
Requires:       perl(Future)
Requires:       perl(Future::AsyncAwait)
%endif
Requires:       perl(threads)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Keyword-Try-%{version}

%if %{without perl_Syntax_Keyword_Try_enables_extra_tests}
for F in t/80await+SKT.t t/80defer+SKT.t t/99pod.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E\b}' MANIFEST
done
%endif

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/Syntax*
%{perl_vendorarch}/Syntax*
%{_mandir}/man3/Syntax::Keyword::Try*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31-2
- Prepare for Oreon 11 (RP1)
