%global source0_hash 947cf41234f88779086f851748a86b04bf6f851f0d84b8950c8e3fbdbf20cd2e
Name:           perl-Net-NBName
Version:        0.26
Release:        1%{?dist}
Summary:        NetBIOS Name Service Requests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-NBName
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMACFARLA/Net-NBName-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Net::NBName is a class that allows you to perform simple NetBIOS Name
Service Requests in your Perl code. It performs these NetBIOS operations
over TCP/IP using Perl's built-in socket support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-NBName-%{version}
for F in bin/* Changes README; do
    sed -i 's/\r//' "$F"
done
for F in bin/*; do
    /usr/bin/perl -pi -e 'print "#!/usr/bin/perl\n\n" if $. == 1' "$F"
done

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
