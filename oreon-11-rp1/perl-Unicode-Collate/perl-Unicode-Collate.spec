%global source0_hash b75dd07bbc252937b1b87064bf79ccd0a1b7ee993b8cf0e80f47406c3205639f
Name:           perl-Unicode-Collate
Version:        1.31
Release:        521%{?dist}
Summary:        Unicode Collation Algorithm
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-DFS-2016
URL:            https://metacpan.org/release/Unicode-Collate
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SADAHIRO/Unicode-Collate-%{version}.tar.gz
Requires:       perl(Unicode::Normalize)
Conflicts:      perl < 4:5.22.0-347
Provides:       perl(Unicode::Collate::Locale)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package is Perl implementation of Unicode Technical Standard #10 (Unicode
Collation Algorithm).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-Collate-%{version}

# Remove pregenerated files
rm Collate/Locale/*
# Collate/CJK/Korean.pm is an input for the mklocale script, do not remove it

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl mklocale
mv Locale/*.pl Collate/Locale
mv Korean.pm Collate/CJK
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
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
%files -n perl-Unicode-Collate-tests -f %{oreon_filedir}/perl-Unicode-Collate-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31-521
- Prepare for Oreon 11 (RP1)
