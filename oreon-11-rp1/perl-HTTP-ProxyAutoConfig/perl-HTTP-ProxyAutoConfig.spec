%global source0_hash 5054f9a90ad2fc3247c84b0b57e8198bd3511bde22711770470c443eb7f1667c
Name:           perl-HTTP-ProxyAutoConfig
Version:        0.3
Release:        1%{?dist}
Summary:        Use a .pac or wpad.dat file to get proxy information
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-ProxyAutoConfig
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MACKENNA/HTTP-ProxyAutoConfig-%{version}.tar.gz
Source1:        LICENSE.correspondence
BuildArch:      noarch
%{?_with_network_tests:
}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
# /oreon:deps
%description
HTTP::ProxyAutoConfig allows perl scripts that need to access the Internet
to determine whether to do so via a proxy server. To do this, it uses proxy
settings provided by an IT department, either on the Web or in a browser's
.pac file on disk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-ProxyAutoConfig-%{version}
cp %{SOURCE1} .

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{?_with_network_tests: make test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
