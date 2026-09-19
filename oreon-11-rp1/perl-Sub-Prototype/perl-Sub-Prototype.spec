%global source0_hash 2b18b1d1464efea7d98b400bdc05150792dd54706418cf7d7177c26ec58691e1

Name:           perl-Sub-Prototype
Version:        0.03
Release:        24%{?dist}
Summary:        Allows you to set a subs prototype
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Prototype
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Sub-Prototype-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ExtraTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This modules allows you to set a subs prototype. It only has one function,
which is exported by default.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sub-Prototype-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENCE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sub*
%{_mandir}/man3/*

%changelog
%autochangelog
