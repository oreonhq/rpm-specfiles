%global source0_hash d2df3dcc5583481c89944e35a15b161e5298020a668a28a3391954f60179cab2

Name:           perl-ServiceNow-API
Version:        1.01
Release:        39%{?dist}
Summary:        ServiceNow API for accessing the Service-now platform

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://wiki.servicenow.com/index.php?title=Perl_API
Source0:        http://wiki.servicenow.com/images/e/e5/ServiceNow-Perl-API.zip
Patch0:         0001-Skip-broken-POD-from-coverage-testing.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(MIME::Type)
BuildRequires:  perl(MIME::Base64)

%{?perl_default_filter}

%description
The Perl API provides a library of Perl classes and sub routines
for programmatic access to the platform and its applications.
The API utilizes the SOAP web service interface of the platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}
%setup -D -T -q -n %{name}-%{version}/ServiceNow-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '.DS_Store' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
