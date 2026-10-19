%global source0_hash c36fd2b68d48c2e17417bf2873c78820f3ae02460fdf5976b8eeab887d59e16c
Name:           perl-Date-Handler
Version:        1.2
Release:        35%{?dist}
Summary:        Easy but complete date object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Handler
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-Handler-%{version}.tar.gz
Patch0:         Date-Handler-1.2-Set-an-encoding-for-POD.patch
BuildArch:      noarch
Requires:       glibc-langpack-en
Recommends:     tzdata
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-es
BuildRequires:  glibc-langpack-fr
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  tzdata
# /oreon:deps
%description
Date::Handler is a container for dates that holds all the methods to
transform itself from a time zone to a time zone and to format itself.

%package Test
Summary:        Test module for Date::Handler
Requires:       %{name} = %{version}-%{release}
Requires:       tzdata
Requires:       glibc-langpack-es
Requires:       glibc-langpack-fr
Conflicts:      perl-Date-Handler < 1.2-18
%description Test
This Perl module provides a series of test cases to be run during the
"make test" of the Date::Handler module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Date-Handler-%{version}
find -type f -exec chmod 0644 {} +
iconv --from=ISO-8859-1 --to=UTF-8 README > README.new
touch -r README README.new
mv README.new README
chmod a+x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --extended_tests
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Date-Handler-Test -f %{oreon_filedir}/perl-Date-Handler-Test.list
%files -n perl-Date-Handler-tests -f %{oreon_filedir}/perl-Date-Handler-tests.list

%changelog

%autochangelog
