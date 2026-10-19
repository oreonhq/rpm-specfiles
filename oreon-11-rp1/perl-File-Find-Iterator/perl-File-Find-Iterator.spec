%global source0_hash a2b87ab9756a2e5bb674adbd39937663ed20c28c716bf5a1095a3ca44d54ab2c
Name:           perl-File-Find-Iterator
Version:        0.4
Release:        42%{?dist}
Summary:        Iterator interface for search files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Find-Iterator
Source0:        https://cpan.metacpan.org/authors/id/T/TE/TEXMEC/File-Find-Iterator-%{version}.tar.gz
Patch0:         File-Find-Iterator-0.4-Fix-parallel-tests.patch
BuildArch:      noarch
Requires:       perl(Class::Iterator) >= 0.1
Requires:       perl(Storable) >= 2.04
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Iterator|Storable)\\)$
Provides:       perl(File::Find::Iterator)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Iterator)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Find::File::Iterator is an iterator object for searching through directory
trees. You can easily run filter on each file name. You can easily save
the search state when you want to stop the search and continue the same
search later.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir File-Find-Iterator-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-File-Find-Iterator-tests -f %{oreon_filedir}/perl-File-Find-Iterator-tests.list

%changelog

%autochangelog
