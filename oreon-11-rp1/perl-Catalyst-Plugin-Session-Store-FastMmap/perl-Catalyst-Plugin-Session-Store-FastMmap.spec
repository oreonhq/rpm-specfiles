%global source0_hash baeb7fd7bf905be74631c88760fd8a2980ceea95627993399581643ef6377274
Name:           perl-Catalyst-Plugin-Session-Store-FastMmap
Version:        0.16
Release:        1%{?dist}
Summary:        FastMmap session storage backend
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-FastMmap
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-Store-FastMmap-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Cache::FastMmap) >= 1.29
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cache::FastMmap)
BuildRequires:  perl(Catalyst::ClassData)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage plugin
for Catalyst that uses an mmap'ed file to act as a shared memory
interprocess cache. It is based on Cache::FastMmap.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-Store-FastMmap-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

TEST_POD=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
