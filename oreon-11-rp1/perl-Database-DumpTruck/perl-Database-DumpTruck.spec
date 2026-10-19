%global source0_hash 98add1bbf9e61ab8280021b35171981cd14d5d525fd89e7629eddbe92f1175b0
Name:           perl-Database-DumpTruck
Version:        1.2
Release:        34%{?dist}
Summary:        Relaxing interface to SQLite
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Database-DumpTruck
Source0:        https://cpan.metacpan.org/authors/id/L/LK/LKUNDRAK/Database-DumpTruck-%{version}.tar.gz
Patch0:         Database-DumpTruck-1.2-sqlite-case-insensitive.patch
Patch1:         Database-DumpTruck-1.2-fix-json-comparison-in-tests.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::JSON)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
%description
This is a simple document-oriented interface to a SQLite database, modelled
after Scraperwiki's Python dumptruck module. It allows for easy (and maybe
inefficient) storage and retrieval of structured data to and from a
database without interfacing with SQL.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Database-DumpTruck-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Database-DumpTruck-tests -f %{oreon_filedir}/perl-Database-DumpTruck-tests.list

%changelog

%autochangelog
