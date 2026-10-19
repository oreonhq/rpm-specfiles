%global source0_hash 66fe80d8fd910b6e5fb8ae2d57c0b59682f3b81cc14d242598a84781425ee480
Name:           perl-HTTP-Recorder
Version:        0.07
Release:        1%{?dist}
Summary:        Record interaction with web sites
License:        GPL-1.0-or-later
URL:            https://metacpan.org/release/HTTP-Recorder
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEMUELF/HTTP-Recorder-%{version}.tar.gz
Patch0:         HTTP-Recorder-0.07-Do-not-use-usr-bin-env.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request::Params)
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Browser-independent recorder for recording interactions with web sites.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Recorder-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
