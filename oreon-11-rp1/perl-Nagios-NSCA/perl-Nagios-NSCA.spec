%global source0_hash 00f216f4a3ebbbff130f9b4bc671246cfb5f1182d258487dbcddfa561d7e4fa5
Name:           perl-Nagios-NSCA
Version:        0.1
Release:        1%{?dist}
Summary:        Nagios::NSCA Perl module
License:        GPL-1.0-or-later 
URL:            https://metacpan.org/release/Nagios-NSCA
Source0:        https://cpan.metacpan.org/modules/by-module/Nagios/Nagios-NSCA-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Digest::CRC)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
# /oreon:deps
%description
Nagios::NSCA Perl module

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Nagios-NSCA-%{version}
# Move the lib to the lib dir.
# http://rt.cpan.org/Public/Bug/Display.html?id=43183
mkdir lib
mv Nagios lib/.

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
chmod 644 bin/send_nsca
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_bindir}/send_nsca
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
