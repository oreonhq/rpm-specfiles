%global source0_hash 4080716c5da7e03b504e3cc0ea1fd5ef9ed6915f6fb737564e9e13d355a89e39
Name:           perl-CPAN-Checksums
Version:        2.14
Release:        1%{?dist}
Summary:        Write a CHECKSUMS file for a directory as on CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Checksums
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/CPAN-Checksums-%{version}.tar.gz
Source1:        A317C15D.pub
BuildArch:      noarch
Requires:       perl(IO::File) >= 1.14
Requires:       perl(Safe)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::File\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gnupg
BuildRequires:  make
BuildRequires:  perl(Compress::Bzip2)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Write a CHECKSUMS file for a directory as on CPAN.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Checksums-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

rm -rf ./elfbins.list ./debugfiles.list ./debuglinks.list ./debugsources.list
export GNUPGHOME=$(mktemp -d)
gpg --import '%{SOURCE1}'
make test
rm -r "$GNUPGHOME"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
