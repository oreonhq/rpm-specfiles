%global source0_hash 618b8ba8f8df1c8ac04d127986a7bb6a834643523000c9c5ea4ee7d95aeef9a8

Name:           maatkit
Version:        7540
Release:        40%{?dist}
Summary:        Essential command-line utilities for MySQL

License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            http://www.maatkit.org/
Source0:        http://maatkit.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(DBD::mysql) >= 1.0
Requires:       perl(Term::ReadKey) >= 2.10

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(ProtocolParser\\)
%global __requires_exclude %__requires_exclude|perl\\(AdvisorRules\\)

%description
This toolkit contains essential command-line utilities for MySQL, such as a 
table checksum tool and query profiler. It provides missing features such as 
checking slaves for data consistency, with emphasis on quality and 
scriptability.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%files
%doc COPYING INSTALL Changelog*
%{_bindir}/*
%{_mandir}/man1/*.1*
%{perl_vendorlib}/%{name}.pod

%changelog
%autochangelog
