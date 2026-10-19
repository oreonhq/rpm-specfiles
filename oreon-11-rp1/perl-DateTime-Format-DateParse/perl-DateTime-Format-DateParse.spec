%global source0_hash f6eca4c8be66ce9992ee150932f8fcf07809fd3d1664caf200b8a5fd3a7e5ebc
Name:           perl-DateTime-Format-DateParse
Version:        0.05
Release:        39%{?dist}
Summary:        Parse Date::Parse compatible formats
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-DateParse
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Date::Parse) >= 2.27
Requires:       perl(DateTime) >= 0.29
Requires:       perl(DateTime::TimeZone) >= 0.27
Requires:       perl(Time::Zone) >= 2.22
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Date::Parse|DateTime(::TimeZone)?|Time::Zone\\)$
# oreon:deps
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module is a DateTime compatibility wrapper around Date::Parse; it allows
one to easily parse formats Date::Parse recognizes for DateTime.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-DateParse-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-DateTime-Format-DateParse-tests -f %{oreon_filedir}/perl-DateTime-Format-DateParse-tests.list

%changelog

%autochangelog
