%global source0_hash 1f2bb9d11414096ab802b3b5028316556b4ecf749631f98910fa25bc5f6da209
%global enable_net_tests 0
Name:           perl-YUM-RepoQuery
Version:        0.002
Release:        1%{?dist}
Summary:        Query a YUM repository for package information
License:        LGPL-2.1-only
URL:            https://metacpan.org/release/YUM-RepoQuery
Source0:        https://backpan.perl.org/authors/id/R/RS/RSRCHBOY/YUM-RepoQuery-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(MooseX::Types::URI)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::DBICSchemaLoaderDigest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(URI::Fetch)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
YUM::RepoQuery takes the URI to a package repository with YUM meta-data, and
allows one to query what packages, and versions of those packages, are
available in that repository.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(ok)
Requires:       perl(Scalar::Util)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

%setup -q -n YUM-RepoQuery-%{version}
# Remove always skipped tests
rm t/release-*
perl -i -ne 'print $_ unless m{^t/release-}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{00-load,01.dbic-md5sum-check}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
%if 0%{enable_net_tests}
export YRQ_LIVE_TESTS=1
%else
unset YRQ_LIVE_TESTS
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{enable_net_tests}
export YRQ_LIVE_TESTS=1
%else
unset YRQ_LIVE_TESTS
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-YUM-RepoQuery-tests -f %{oreon_filedir}/perl-YUM-RepoQuery-tests.list

%changelog

%autochangelog
