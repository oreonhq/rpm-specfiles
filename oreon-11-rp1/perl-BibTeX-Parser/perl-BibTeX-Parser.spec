%global source0_hash 6ea3682cd6ecb91a772d7c233366f1a51258253997a208d1451deda56487a5ca
%bcond_without perl_BibTeX_Parser_enables_optional_test
Name:           perl-BibTeX-Parser
Version:        1.93
Release:        1%{?dist}
Summary:        Pure Perl BibTeX parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BibTeX-Parser
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BORISV/BibTeX-Parser-%{version}.tar.gz
Patch0:         BibTeX-Parser-1.03-Remove-a-debugging-output-from-BibTeX-Parser-Entry-t.patch
BuildArch:      noarch
%global latex_to_unicode_min_ver 0.11
%if %{with perl_BibTeX_Parser_enables_optional_test}
%endif
Requires:       perl(LaTeX::ToUnicode) >= %{latex_to_unicode_min_ver}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((LaTeX::ToUnicode|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(LaTeX::ToUnicode)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a BibTeX parser written in Perl.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n BibTeX-Parser-%{version}
# Remove skipped tests
for F in t/08-parse_large.t t/release-pod-*.t \
%if %{without perl_BibTeX_Parser_enables_optional_test}
t/pod.t t/pod-coverage.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Correct the permissions
chmod a+x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_BibTeX_Parser_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t \
    %{buildroot}%{_libexecdir}/%{name}/t/pod-coverage.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-BibTeX-Parser-tests -f %{oreon_filedir}/perl-BibTeX-Parser-tests.list

%changelog

%autochangelog
