%global source0_hash 4d2578073748cc774b755f9805697221753b38154f0f57b7d820140128b4a9b1

Name:           perl-Format-Human-Bytes
Version:        0.06
Release:        43%{?dist}
Summary:        Format a bytecount and make it human readable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Format-Human-Bytes
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEWI/Format-Human-Bytes-%{version}.tar.gz
Patch0:         Format-Human-Bytes-no-autoinstall.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)

%description
This module returns you a printable string which is more readable by humans than 
a simple bytecount.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Format-Human-Bytes-%{version}
%patch -P0 -p1 -b .noautoinstall

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
