%global source0_hash 93ebdfaaefcfe9ab683f0121c85f24475d8197f0bcec46018219e4111434dde3
Name:           perl-Crypt-MySQL
Version:        0.04
Release:        1%{?dist}
Summary:        Emulate MySQL PASSWORD() function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-MySQL
Source0:        https://cpan.metacpan.org/authors/id/I/IK/IKEBE/Crypt-MySQL-%{version}.tar.gz
Requires:       perl(Exporter)
Requires:       perl(XSLoader)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Crypt::MySQL emulates MySQL PASSWORD() SQL function, without
libmysqlclient. You can compare encrypted passwords, without real MySQL
environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Crypt-MySQL-%{version}
%oreon_prep
%build

%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
