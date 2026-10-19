%global source0_hash 28797f8e427406720584cafd10e780a78ec2b569c555a18743d74553d5f5083f
Name:           perl-Growl-GNTP
Version:        0.21
Release:        1%{?dist}
Summary:        Perl implementation of GNTP Protocol (Client Part)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Growl-GNTP
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTN/Growl-GNTP-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
Growl::GNTP is Perl implementation of GNTP Protocol (Client Part).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Growl-GNTP-%{version}
%oreon_prep
%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
