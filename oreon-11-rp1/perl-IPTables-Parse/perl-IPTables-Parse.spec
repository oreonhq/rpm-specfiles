%global source1_hash 4436bc04dc367635981e773bae3d9c4abe2083264dc5cab5ae0044e515fbb4b3
%global source0_hash 0769cacf8997e99f89b602377996205dc3692030534c395471fa1ebce263dac8
Name:           perl-IPTables-Parse
Version:        1.6.1
Release:        1%{?dist}
Summary:        Perl extension for parsing iptables firewall rulesets
License:        Artistic-2.0
URL:            http://www.cipherdyne.org/modules/
Source0:        http://www.cipherdyne.org/modules/IPTables-Parse-%{version}.tar.bz2
Source1:        http://www.cipherdyne.org/modules/IPTables-Parse-%{version}.tar.bz2.asc
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The IPTables::Parse package provides an interface to parse iptables rules
on Linux systems through the direct execution of iptables commands, or from
parsing a file that contains an iptables policy listing. You can get the
current policy applied to a table/chain, look for a specific user-defined
chain, check for a default DROP policy, or determing whether or not logging
rules exist.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPTables-Parse-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
