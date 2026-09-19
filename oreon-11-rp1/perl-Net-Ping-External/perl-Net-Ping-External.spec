%global source0_hash aad917fc678e774670b2b94072fd368d97fc09537f2cc802ea2b51398dec04fb

Name:           perl-Net-Ping-External
Version:        0.15
Release:        35%{?dist}
Summary:        Cross-platform interface to ICMP "ping" utilities
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Ping-External
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Ping-External-%{version}.tar.gz
# https://github.com/chorny/Net-Ping-External/issues/6
# Patch based on http://matthias.sdfeu.org/devel/net-ping-external-cmd-injection.patch
Patch0:         perl-Net-Ping-External-CVE-2008-7319.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Net::Ping::External is a module which interfaces with the "ping" command on
many systems. It presently provides a single function, ping(), that takes
in a hostname and (optionally) a timeout and returns true if the host is
alive, and false otherwise. Unless you have the ability (and willingness)
to run your scripts as the superuser on your system, this module will
probably provide more accurate results than Net::Ping will.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Ping-External-%{version}
%patch -P0 -p1 -b .CVE-2008-7319

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

for i in Changes README ToDo; do
    sed -i 's/\r//' "$i"
done

%check
%{?_with_network_tests: make test }

%files
%doc Changes README ToDo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
