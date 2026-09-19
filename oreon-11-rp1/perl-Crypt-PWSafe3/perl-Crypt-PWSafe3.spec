%global source0_hash 9906f69af2f9477c29820712e18333e521cbbad866c5e2893f9420789af29373

%global snapshot 1
%global OWNER TLINDEN
%global PROJECT Crypt--PWSafe3
%global commit 002b0f0462a990b64c004a14151257273d637599
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20220227

Name:           perl-Crypt-PWSafe3
Version:        1.23%{?snapshot:~%{commitdate}git%{shortcommit}}
Release:        12%{?dist}
Summary:        Read and write Passwordsafe v3 files
License:        Artistic-2.0
URL:            https://metacpan.org/release/Crypt-PWSafe3
%if 0%{?snapshot}
Source0:        https://github.com/%{OWNER}/%{PROJECT}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-PWSafe3-%{version}.tar.gz
%endif
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Bytes::Random::Secure)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::CBC) >= 2.3
BuildRequires:  perl(Crypt::ECB) >= 1.45
BuildRequires:  perl(Crypt::Twofish) >= 2.14
BuildRequires:  perl(Data::Dumper)
# Data::UUID 1.217 rounded two 2 digits
BuildRequires:  perl(Data::UUID) >= 1.22
BuildRequires:  perl(Digest::HMAC) >= 1
BuildRequires:  perl(Digest::SHA) >= 1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Bytes::Random::Secure)
Requires:       perl(Crypt::CBC) >= 2.3
Requires:       perl(Crypt::ECB) >= 1.45
Requires:       perl(Crypt::Twofish) >= 2.14
# Data::UUID 1.217 rounded two 2 digits
Requires:       perl(Data::UUID) >= 1.22
Requires:       perl(Digest::HMAC) >= 1
Requires:       perl(Digest::SHA) >= 1

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Crypt::CBC\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Crypt::ECB\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Crypt::Random\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Crypt::Twofish\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Data::UUID\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Digest::HMAC\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Digest::SHA\\)$

%description
Crypt::PWSafe3 provides read and write access to password database files
created by Password Safe V3 (and up) available at <http://passwordsafe.sf.net>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?snapshot}
%autosetup -n %{PROJECT}-%{commit}
%else
%autosetup -p1 -n Crypt-PWSafe3-%{version}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
