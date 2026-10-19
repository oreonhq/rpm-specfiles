%global source0_hash e7f4e7e7052d6073b6dcf49a37035ba5a5144e848071fc9292461a83c3cdddfd
%global have_cassandra 0
%global have_redis     1
Name:		perl-Apache-Session-NoSQL
Version:	0.3
Release:        1%{?dist}
Summary:        (Deprecated) NoSQL implementation of Apache::Session
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Apache-Session-NoSQL
Source0:        https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-NoSQL-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Session::Generate::MD5)
BuildRequires:  perl(Apache::Session::Lock::Null)
BuildRequires:  perl(Apache::Session::Serialize::Base64)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Redis)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
NoSQL implementation of Apache::Session. Sessions are stored in NoSQL
bases, either Redis or Cassandra.

Note that this package is deprecated and Apache::Session::Browseable should
be used in preference to it.

%package -n perl-Apache-Session-Redis
Summary:	Redis driver for Apache::Session::NoSQL
BuildRequires:	perl(Redis)
Requires:	perl-Apache-Session-NoSQL = %{version}-%{release}
Provides:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}
%description -n perl-Apache-Session-Redis
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Session-NoSQL-%{version}

%if ! %{have_cassandra} && ! %{have_redis}
%{error:At least one of Cassandra or Redis must be available}
exit 1
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles perl-Apache-Session-Redis usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Apache-Session-Redis -f %{oreon_filedir}/perl-Apache-Session-Redis.list

%changelog

%autochangelog
