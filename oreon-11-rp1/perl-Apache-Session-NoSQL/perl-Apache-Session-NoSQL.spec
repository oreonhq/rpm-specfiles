%global source0_hash e7f4e7e7052d6073b6dcf49a37035ba5a5144e848071fc9292461a83c3cdddfd

# Support drivers based on what's available
%global have_cassandra 0
%global have_redis     1

Name:		perl-Apache-Session-NoSQL
Version:	0.3
Release:	8%{?dist}
Summary:	(Deprecated) NoSQL implementation of Apache::Session
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Apache-Session-NoSQL
Source0:	https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-NoSQL-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Apache::Session)
BuildRequires:	perl(Apache::Session::Generate::MD5)
BuildRequires:	perl(Apache::Session::Lock::Null)
BuildRequires:	perl(Apache::Session::Serialize::Base64)
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test::More)
# Runtime
Requires:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}

%description
NoSQL implementation of Apache::Session. Sessions are stored in NoSQL
bases, either Redis or Cassandra.

Note that this package is deprecated and Apache::Session::Browseable should
be used in preference to it.

%if %{have_cassandra}
%package -n perl-Apache-Session-Cassandra
Summary:	Cassandra driver for Apache::Session::NoSQL
BuildRequires:	perl(Net::Cassandra)
Requires:	perl-Apache-Session-NoSQL = %{version}-%{release}
Provides:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}

%description -n perl-Apache-Session-Cassandra
%{summary}.
%endif

%if %{have_redis}
%package -n perl-Apache-Session-Redis
Summary:	Redis driver for Apache::Session::NoSQL
BuildRequires:	perl(Redis)
Requires:	perl-Apache-Session-NoSQL = %{version}-%{release}
Provides:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}

%description -n perl-Apache-Session-Redis
%{summary}.
%endif

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

%check
make test

%files
%doc Changes examples/
%dir %{perl_vendorlib}/Apache/
%dir %{perl_vendorlib}/Apache/Session/
%dir %{perl_vendorlib}/Apache/Session/Store/
%dir %{perl_vendorlib}/Apache/Session/Store/NoSQL/
%{perl_vendorlib}/Apache/Session/NoSQL.pm
%{perl_vendorlib}/Apache/Session/Store/NoSQL.pm
%{_mandir}/man3/Apache::Session::NoSQL.3*
%{_mandir}/man3/Apache::Session::Store::NoSQL.3*

%if %{have_cassandra}
%files -n perl-Apache-Session-Cassandra
%{perl_vendorlib}/Apache/Session/Cassandra.pm
%{perl_vendorlib}/Apache/Session/Store/NoSQL/Cassandra.pm
%{_mandir}/man3/Apache::Session::Cassandra.3*
%{_mandir}/man3/Apache::Session::Store::NoSQL::Cassandra.3*
%else
%exclude %{perl_vendorlib}/Apache/Session/Cassandra.pm
%exclude %{perl_vendorlib}/Apache/Session/Store/NoSQL/Cassandra.pm
%exclude %{_mandir}/man3/Apache::Session::Cassandra.3*
%exclude %{_mandir}/man3/Apache::Session::Store::NoSQL::Cassandra.3*
%endif

%if %{have_redis}
%files -n perl-Apache-Session-Redis
%{perl_vendorlib}/Apache/Session/Redis.pm
%{perl_vendorlib}/Apache/Session/Store/NoSQL/Redis.pm
%{_mandir}/man3/Apache::Session::Redis.3*
%{_mandir}/man3/Apache::Session::Store::NoSQL::Redis.3*
%else
%exclude %{perl_vendorlib}/Apache/Session/Redis.pm
%exclude %{perl_vendorlib}/Apache/Session/Store/NoSQL/Redis.pm
%exclude %{_mandir}/man3/Apache::Session::Redis.3*
%exclude %{_mandir}/man3/Apache::Session::Store::NoSQL::Redis.3*
%endif

%changelog
%autochangelog
