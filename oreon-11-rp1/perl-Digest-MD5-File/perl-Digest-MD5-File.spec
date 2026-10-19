%global source0_hash adb43a54e32627b4f7e57c9640e6eb06d0bb79d8ea54cd0bd79ed35688fb1218
Name:		perl-Digest-MD5-File
Version:	0.08
Release:        1%{?dist}
Summary:        Perl extension for getting MD5 sums for files and URLs
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Digest-MD4
Source0:        https://cpan.metacpan.org/modules/by-module/Digest/Digest-MD5-File-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Encode)
Requires:	perl(Exporter)
Requires:	perl(File::Spec)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Get MD5 sums for files of a given path or content of a given URL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Digest-MD5-File-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
