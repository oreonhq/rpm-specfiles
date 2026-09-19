%global source0_hash ca8e160daff164bfb99be8b7467a83059906725fada91d75f256917b3d313400

Name:		nsdiff
Version:	1.85
Release:	4%{?dist}
Summary:	create an "nsupdate" script from DNS zone file differences

License:	0BSD OR MIT-0
URL:		https://dotat.at/prog/nsdiff/
# Alternative:
#Source0:	https://github.com/fanf2/%%{name}/archive/%%{name}-%%{version}.tar.gz
Source0:	https://dotat.at/prog/%{name}/DNS-%{name}-%{version}.tar.gz

BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl(:VERSION) >= 5.10
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Pod::Man)
BuildRequires:	perl(Pod::Html)
BuildArch:	noarch
Requires:	bind-utils
Requires:	perl(:VERSION) >= 5.10

%description
The nsdiff program examines the old and new versions of a DNS zone, and
outputs the differences as a script for use by BIND's nsupdate program.
It provides a bridge between static zone files and dynamic updates.

The nspatch script is a wrapper around `nsdiff | nsupdate` that checks
and reports errors in a manner suitable for running from cron.

The nsvi script makes it easy to edit a dynamic zone.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n DNS-%{name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%files
%doc README*
%{_bindir}/ns*
%{_mandir}/man1/ns*.1*
%{_mandir}/man3/DNS::ns*.3*
%{perl_vendorlib}/*

%changelog
%autochangelog
