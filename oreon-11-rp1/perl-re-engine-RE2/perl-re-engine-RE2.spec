%global source0_hash b317fd54e25d1c67e41f84725d232f3688cdea4ab686e6095984f6fc932c5fa1

Name:           perl-re-engine-RE2
Summary:        RE2 regex engine
Version:        0.18
Release:        14%{?dist}
# lib/re/engine/RE2.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# ppport.h:             GPL-1.0-or-later OR Artistic-1.0-Perl
# README:               GPL-1.0-or-later OR Artistic-1.0-Perl
## Unbundled and never used:
# re2/BUILD:                BSD-like, see LICENSE
# re2/CMakeLists.txt:       BSD-like, see LICENSE
# re2/doc/mksyntaxgo:       BSD-like, see LICENSE
# re2/lib/git/commit-msg.hook:  Apache-2.0
# re2/LICENSE:              BSD-3-Clause text
# re2/Makefile:             BSD-like, see LICENSE
# re2/re2/bitmap256.h:      BSD-like, see LICENSE
# re2/re2/bitstate.cc:      BSD-like, see LICENSE
# re2/re2/dfa.cc:           BSD-like, see LICENSE
# re2/re2/filtered_re2.cc:  BSD-like, see LICENSE
# re2/re2/filtered_re2.h:   BSD-like, see LICENSE
# re2/re2/fuzzing/compiler-rt/include/fuzzer/FuzzedDataProvider.h:  Apache-2.0 WITH LLVM-exception
# re2/re2/fuzzing/compiler-rt/LICENSE:  Apache-2.0 WITH LLVM-exception text
# re2/re2/fuzzing/re2_fuzzer.cc:    BSD-like, see LICENSE
# re2/re2/make_perl_groups.pl:      BSD-like, see LICENSE
# re2/re2/make_unicode_casefold.py: BSD-like, see LICENSE
# re2/re2/make_unicode_groups.py:   BSD-like, see LICENSE
# re2/re2/mimics_pcre.cc:       BSD-like, see LICENSE
# re2/re2/nfa.cc:               BSD-like, see LICENSE
# re2/re2/onepass.cc:           BSD-like, see LICENSE
# re2/re2/parse.cc:             BSD-like, see LICENSE
# re2/re2/perl_groups.cc:       generated from make_perl_groups.pl
# re2/re2/pod_array.h:          BSD-like, see LICENSE
# re2/re2/prefilter.cc:         BSD-like, see LICENSE
# re2/re2/prefilter.h:          BSD-like, see LICENSE
# re2/re2/prefilter_tree.cc:    BSD-like, see LICENSE
# re2/re2/prefilter_tree.h:     BSD-like, see LICENSE
# re2/re2/prog.cc:              BSD-like, see LICENSE
# re2/re2/prog.h:               BSD-like, see LICENSE
# re2/re2/re2.cc:               BSD-like, see LICENSE
# re2/re2/re2.h:                BSD-like, see LICENSE
# re2/re2/regexp.cc:            BSD-like, see LICENSE
# re2/re2/regexp.h:             BSD-like, see LICENSE
# re2/re2/set.cc:               BSD-like, see LICENSE
# re2/re2/set.h:                BSD-like, see LICENSE
# re2/re2/simplify.cc:          BSD-like, see LICENSE
# re2/re2/sparse_array.h:       BSD-like, see LICENSE
# re2/re2/sparse_set.h:         BSD-like, see LICENSE
# re2/re2/stringpiece.cc:       BSD-like, see LICENSE
# re2/re2/stringpiece.h:        BSD-like, see LICENSE
# re2/re2/testing/backtrack.cc:         BSD-like, see LICENSE
# re2/re2/testing/charclass_test.cc:    BSD-like, see LICENSE
# re2/re2/testing/compile_test.cc:      BSD-like, see LICENSE
# re2/re2/testing/dfa_test.cc:          BSD-like, see LICENSE
# re2/re2/testing/dump.cc:              BSD-like, see LICENSE
# re2/re2/testing/exhaustive_test.cc:   BSD-like, see LICENSE
# re2/re2/testing/exhaustive_tester.cc  BSD-like, see LICENSE
# re2/re2/testing/exhaustive_tester.h:  BSD-like, see LICENSE
# re2/re2/testing/exhaustive1_test.cc:  BSD-like, see LICENSE
# re2/re2/testing/exhaustive2_test.cc:  BSD-like, see LICENSE
# re2/re2/testing/exhaustive3_test.cc:  BSD-like, see LICENSE
# re2/re2/testing/filtered_re2_test.cc: BSD-like, see LICENSE
# re2/re2/testing/mimics_pcre_test.cc:  BSD-like, see LICENSE
# re2/re2/testing/null_walker.cc:       BSD-like, see LICENSE
# re2/re2/testing/parse_test.cc:        BSD-like, see LICENSE
# re2/re2/testing/possible_match_test.cc:   BSD-like, see LICENSE
# re2/re2/testing/random_test.cc:       BSD-like, see LICENSE
# re2/re2/testing/regexp_benchmark.cc:  BSD-like, see LICENSE
# re2/re2/testing/regexp_generator.cc:  BSD-like, see LICENSE
# re2/re2/testing/regexp_generator.h:   BSD-like, see LICENSE
# re2/re2/testing/regexp_test.cc:       BSD-like, see LICENSE
# re2/re2/testing/required_prefix_test.cc:  BSD-like, see LICENSE
# re2/re2/testing/re2_arg_test.cc:      BSD-like, see LICENSE
# re2/re2/testing/re2_test.cc:          BSD-like, see LICENSE
# re2/re2/testing/search_test.cc:       BSD-like, see LICENSE
# re2/re2/testing/set_test.cc:          BSD-like, see LICENSE
# re2/re2/testing/simplify_test.cc:     BSD-like, see LICENSE
# re2/re2/testing/string_generator.cc:  BSD-like, see LICENSE
# re2/re2/testing/string_generator.h:   BSD-like, see LICENSE
# re2/re2/testing/string_generator_test.cc: BSD-like, see LICENSE
# re2/re2/testing/tester.cc:            BSD-like, see LICENSE
# re2/re2/testing/tester.h:             BSD-like, see LICENSE
# re2/re2/tostring.cc:          BSD-like, see LICENSE
# re2/re2/unicode_casefold.cc:  generated from make_unicode_casefold.py
# re2/re2/unicode_casefold.h:   BSD-like, see LICENSE
# re2/re2/unicode_groups.cc:    generated from make_unicode_groups.py
# re2/re2/unicode_groups.h:     BSD-like, see LICENSE
# re2/re2/unicode.py:           BSD-like, see LICENSE
# re2/re2/walker-inl.h:         BSD-like, see LICENSE
# re2/testinstall.cc:           BSD-like, see LICENSE
# re2/util/benchmark.cc:        BSD-like, see LICENSE
# re2/util/benchmark.h:         BSD-like, see LICENSE
# re2/util/flags.h:             BSD-like, see LICENSE
# re2/util/fuzz.cc:             BSD-like, see LICENSE
# re2/util/logging.h:           BSD-like, see LICENSE
# re2/util/malloc_counter.h:    BSD-like, see LICENSE
# re2/util/mix.h:               BSD-like, see LICENSE
# re2/util/mutex.h:             BSD-like, see LICENSE
# re2/util/pcre.cc:             BSD-like, see LICENSE
# re2/util/pcre.h:              BSD-like, see LICENSE
# re2/util/rune.cc:     dtoa
# re2/util/strutil.cc:          BSD-like, see LICENSE
# re2/util/strutil.h:           BSD-like, see LICENSE
# re2/util/test.h:              BSD-like, see LICENSE
# re2/util/utf.h:       dtoa
# re2/util/util.h:              BSD-like, see LICENSE
# re2/WORKSPACE:                BSD-like, see LICENSE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND dtoa
URL:            https://metacpan.org/release/re-engine-RE2
Source0:        https://cpan.metacpan.org/authors/id/D/DG/DGL/re-engine-RE2-%{version}.tar.gz
# Discussion started with upstream at
# <https://rt.cpan.org/Public/Bug/Display.html?id=83467>
Patch0:         re-engine-RE2-0.18-Unbundle-re2.patch
# Adapt to re2-20240702, bug #2304727, CPAN RT#83467
Patch1:         re-engine-RE2-0.18-Use-C-17.patch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# (This is a leaf package on i686 because all dependent packages are noarch,
# and noarch packages no longer build on i686.)
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:    %{ix86}
%endif
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  re2-devel
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README TODO
%dir %{perl_vendorarch}/auto/re
%dir %{perl_vendorarch}/auto/re/engine
%{perl_vendorarch}/auto/re/engine/RE2
%dir %{perl_vendorarch}/re
%dir %{perl_vendorarch}/re/engine
%{perl_vendorarch}/re/engine/RE2.pm
%{_mandir}/man3/re::engine::RE2.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
