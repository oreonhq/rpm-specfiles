%global source0_hash c30c688027a52ff4f58cd69d6d8ef35472a7cf106d4ce94eb73a796ba7c7ffa7

Name:           perl-File-KeePass
Version:        2.03
Release:        39%{?dist}
Summary:        Interface to KeePass V1 and V2 database files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-KeePass
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/File-KeePass-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Crypt::Rijndael) 
BuildRequires:  perl(Digest::SHA) 
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(Compress::Raw::Zlib)
Requires:       perl(Crypt::Rijndael) 
Requires:       perl(Digest::SHA) 
Requires:       perl(XML::Parser)
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(MIME::Base64)

%description
File::KeePass gives access to KeePass version 1 (kdb) and 
version 2 (kdbx) databases.

The version 1 and version 2 databases are very different 
in construction, but the majority of information overlaps 
and many algorithms are similar. File::KeePass attempts to 
iron out as many of the differences.

File::KeePass gives nearly raw data access. There are a few
 utility methods for manipulating groups and entries. More 
advanced manipulation can easily be layered on top by 
other modules.

File::KeePass is only used for reading and writing databases
and for keeping passwords scrambled while in memory. 
Programs dealing with UI or using of auto-type features are
the domain of other modules on CPAN. File::KeePass::Agent 
is one example.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-KeePass-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
