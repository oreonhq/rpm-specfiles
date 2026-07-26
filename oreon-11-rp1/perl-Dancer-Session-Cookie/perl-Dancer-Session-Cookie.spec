%global source0_hash 526790cf91b8d2501a58292284bf511a2f00b05f51aa0aff713ff5166b4d6412

# Run optional test
%bcond_without perl_Dancer_Session_Cookie_enables_optional_test

Name:           perl-Dancer-Session-Cookie
Version:        0.30
Release:        25%{?dist}
Summary:        Encrypted cookie-based session back-end for Dancer
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dancer-Session-Cookie
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Dancer-Session-Cookie-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Dancer) >= 1.3113
BuildRequires:  perl(Dancer::Cookie)
BuildRequires:  perl(Dancer::Cookies)
BuildRequires:  perl(Dancer::Session::Abstract)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(parent)
BuildRequires:  perl(PerlX::Maybe)
BuildRequires:  perl(Session::Storage::Secure) >= 0.010
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::CRC32)
BuildRequires:  perl(Time::Duration::Parse)
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(Dancer::ModuleLoader)
BuildRequires:  perl(Dancer::Test)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Requires)
%if %{with perl_Dancer_Session_Cookie_enables_optional_test}
# Optional tests:
# CPAN::Meta not useful
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack) >= 1.0029
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(YAML)
%endif

%description
This module implements a session engine for sessions stored entirely in
cookies. Usually only session ID is stored in cookies and the session data
itself are saved in some external storage, e.g. database. This module allows to
avoid using external storage at all.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer-Session-Cookie-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md CONTRIBUTORS README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
