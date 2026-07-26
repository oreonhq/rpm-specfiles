%global source0_hash aa721a521eab1acba6c0d7981eea1aa0392756a441cd41d475ec983efc0f937f

Name:           perl-CGI-Application-Plugin-SuperForm
Version:        0.5
Release:        45%{?dist}
Summary:        Create sticky forms with HTML::SuperForm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-SuperForm
Source0:        https://cpan.metacpan.org/authors/id/V/VA/VANAMBURG/CGI-Application-Plugin-SuperForm-%{version}.tar.gz
# Fix using of UNIVERSAL for Perl 5.22 (RT#97686)
Patch1:         CGI-Application-Plugin-SuperForm-0.5-RT-97686-Fix-using-of-UNIVERSAL.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::SuperForm)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
Create sticky HTML forms in CGI::Application run modes using HTML::SuperForm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-SuperForm-%{version}
%patch -P1 -p1

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
%doc Changes EXAMPLES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
