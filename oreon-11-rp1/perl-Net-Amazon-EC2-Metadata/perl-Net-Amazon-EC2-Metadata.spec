%global source0_hash 64221d2db296b9ac7f5a0e2a002797311f06200cc8c93d97f05678869b1f3411

Name:           perl-Net-Amazon-EC2-Metadata
Version:        0.10
Release:        42%{?dist}
Summary:        Retrieves data from EC2 Metadata service
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Amazon-EC2-Metadata
Source0:        https://cpan.metacpan.org/authors/id/N/NM/NMCFARL/Net-Amazon-EC2-Metadata-%{version}.tar.gz
Patch0:         perl-Net-Amazon-EC2-Metadata-0.10-say.patch
# https://rt.cpan.org/Public/Bug/Display.html?id=74949
Patch1:         net-amazon-ec2-metadata.diff
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
This module queries Amazon's Elastic Compute Cloud Metadata service.
It also fetches 'user_data' which follows the same API but is often no
considered part of the metadata service by Amazons documentation. The
module also ships with a command line tool ec2meta that provides the same
data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Amazon-EC2-Metadata-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
