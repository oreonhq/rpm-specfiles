%global source0_hash 4080716c5da7e03b504e3cc0ea1fd5ef9ed6915f6fb737564e9e13d355a89e39

Name:           perl-CPAN-Checksums
Version:        2.14
Release:        12%{?dist}
Summary:        Write a CHECKSUMS file for a directory as on CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Checksums
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/CPAN-Checksums-%{version}.tar.gz
# Upstream's key to verify MANIFEST, bug #1083915
Source1:        A317C15D.pub
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Compress::Bzip2)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5) >= 2.36
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(Safe)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  coreutils
BuildRequires:  gnupg
# Config not used
# Digest::SHA1 not used if Digest::SHA is available
# Digest::SHA::PurePerl not used if Digest::SHA is available
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Module::Signature) >= 0.79
# Time::HiRes not useful
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.18
Requires:       perl(IO::File) >= 1.14
Requires:       perl(Safe)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::File\\)$

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

%check
# test checks MANIFEST -  would fail because of debug files
rm -rf ./elfbins.list ./debugfiles.list ./debuglinks.list ./debugsources.list
export GNUPGHOME=$(mktemp -d)
gpg --import '%{SOURCE1}'
make test
rm -r "$GNUPGHOME"

%files
%doc Changes README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
