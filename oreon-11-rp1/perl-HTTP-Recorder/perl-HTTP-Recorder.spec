%global source0_hash 66fe80d8fd910b6e5fb8ae2d57c0b59682f3b81cc14d242598a84781425ee480

Name:           perl-HTTP-Recorder
Version:        0.07
Release:        31%{?dist}
Summary:        Record interaction with web sites

License:        GPL-1.0-or-later
URL:            https://metacpan.org/release/HTTP-Recorder
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEMUELF/HTTP-Recorder-%{version}.tar.gz
# Use real interpreter instead of indirect call via /usr/bin/env
Patch0:         HTTP-Recorder-0.07-Do-not-use-usr-bin-env.patch

BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
# Getopt::Long not used at tests
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
# HTTP::Proxy not used at tests
BuildRequires:  perl(HTTP::Request::Params)
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::UserAgent)
# Pod::Usage not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 0.95

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

%check
make test

%files
%doc CHANGES README
%{_bindir}/httprecorder
%{perl_vendorlib}/HTTP/
%{_mandir}/man1/httprecorder*
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
