%global source0_hash c9ecc13376d0ff7dba481977337c33ea74e5d266a428b6af31552a2919ef7ef8

Name:           perl-MooseX-MarkAsMethods
Version:        0.15
Release:        38%{?dist}
Summary:        Mark overload code symbols as methods
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://metacpan.org/release/MooseX-MarkAsMethods/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-MarkAsMethods-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean) >= 0.12
# Tests only:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.92

Provides:       perl(MooseX::MarkAsMethods)
Provides:       perl(MooseX::MarkAsMethods)
%description
MooseX::MarkAsMethods allows one to easily mark certain functions as Moose
methods. This will allow other packages such as namespace::autoclean to
operate without blowing away your overloads. After using
MooseX::MarkAsMethods your overloads will be recognized by Class::MOP as
being methods, and class extension as well as composition from roles with
overloads will "just work".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-MarkAsMethods-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
