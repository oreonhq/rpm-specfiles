%global source0_hash 002326bed663b4c30e68e0f8f55fedf8fe98e50a8295e9a4be6185886bf722ff

Name:           perl-IPTables-ChainMgr
Version:        1.6
Release:        29%{?dist}
Summary:        Perl extension for manipulating iptables policies
License:        Artistic-2.0
URL:            http://www.cipherdyne.org/modules/
Source0:        http://www.cipherdyne.org/modules/IPTables-ChainMgr-%{version}.tar.bz2
Source1:        http://www.cipherdyne.org/modules/IPTables-ChainMgr-%{version}.tar.bz2.asc
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPTables::Parse)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)

%description
The IPTables::ChainMgr package provides an interface to manipulate iptables
policies on Linux systems through the direct execution of iptables
commands. Although making a perl extension of libiptc provided by the iptables
project is possible, it is easy to just execute iptables commands directly in
order to both parse and change the configuration of the policy. Further, this
simplifies installation since the only external requirement is (in the spirit
of scripting) to be able to point IPTables::ChainMgr at an installed iptables
binary instead of having to compile against a library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPTables-ChainMgr-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
