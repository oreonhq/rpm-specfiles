%global source0_hash 20bbc16cb3454fe5e8cf34fe61f1a91fe26c3f17e449ff665fcbbb92ab443ebd
Name:           perl-AWS-Signature4
Version:        1.02
Release:        1%{?dist}
Summary:        Create a version4 signature for Amazon Web Services
License:        GPL-1.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/AWS-Signature4
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/AWS-Signature4-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Digest::SHA) >= 5.47
Requires:       perl(URI) >= 1.59
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Digest::SHA|URI)\\)$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implement's Amazon Web Service's Signature version 4
(http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AWS-Signature4-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
