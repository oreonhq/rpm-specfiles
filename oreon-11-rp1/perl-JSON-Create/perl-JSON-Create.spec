%global source0_hash 5faefe0d833b8132568865308f3239d3cdaa1b8a1ecc9b5624dcf1efbe10683e
%bcond_without perl_JSON_Create_enables_optional_tests
Name:           perl-JSON-Create
Version:        0.35
Release:        17%{?dist}
Summary:        Create JSON
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/JSON-Create
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/JSON-Create-%{version}.tar.gz
%if %{with perl_JSON_Create_enables_optional_tests}
%endif
Requires:       perl(JSON::Parse) >= 0.60
Requires:       perl(Unicode::UTF8) >= 0.62
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Unicode::UTF8\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(JCT\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(JCT\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::Parse)
BuildRequires:  perl(JSON::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(Unicode::UTF8)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(boolean)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Test-Harness
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
JSON::Create encodes Perl variables into JSON. The basic routine "create_json"
gives common defaults. The stricter version "create_json_strict" accepts only
unambiguous inputs. For more customization, an object created with "new" and
run with "create" allows specifying behavior in more detail.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_JSON_Create_enables_optional_tests}
Requires:       perl(boolean)
Requires:       perl(JSON::PP)
Requires:       perl(JSON::Tiny)
Requires:       perl(Types::Serialiser)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n JSON-Create-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 &&
!s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd  %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset JSONCreatePP
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-JSON-Create-tests -f %{oreon_filedir}/perl-JSON-Create-tests.list

%changelog

%autochangelog
