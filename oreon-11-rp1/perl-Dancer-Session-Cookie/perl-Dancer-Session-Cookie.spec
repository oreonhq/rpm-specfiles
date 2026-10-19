%global source0_hash 526790cf91b8d2501a58292284bf511a2f00b05f51aa0aff713ff5166b4d6412
%bcond_without perl_Dancer_Session_Cookie_enables_optional_test
Name:           perl-Dancer-Session-Cookie
Version:        0.30
Release:        1%{?dist}
Summary:        Encrypted cookie-based session back-end for Dancer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dancer-Session-Cookie
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Dancer-Session-Cookie-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dancer_Session_Cookie_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Dancer)
BuildRequires:  perl(Dancer::Cookie)
BuildRequires:  perl(Dancer::Cookies)
BuildRequires:  perl(Dancer::ModuleLoader)
BuildRequires:  perl(Dancer::Session::Abstract)
BuildRequires:  perl(Dancer::Test)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(PerlX::Maybe)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Session::Storage::Secure)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::CRC32)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(YAML)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
