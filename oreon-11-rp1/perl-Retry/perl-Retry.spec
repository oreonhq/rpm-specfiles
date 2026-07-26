%global source0_hash ff5eb6be53e311202b9cf671c05fd6094b6d0a2366720abbf35f6606828d16a3

Name:           perl-Retry
Version:        1.03
Release:        26%{?dist}
Summary:        Perl function wrapper providing exponential back-off and callbacks on failure
License:        Artistic-2.0
URL:            https://metacpan.org/release/Retry
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJC/Retry-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Find)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(warnings)
BuildRequires:  sed

%description
A one-feature module, this provides a method to wrap any function in
automatic retry logic, with exponential back-off delays, and a callback
for each time an attempt fails.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Retry-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
