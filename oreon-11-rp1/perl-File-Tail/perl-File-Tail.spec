%global source0_hash 26d09f81836e43eae40028d5283fe5620fe6fe6278bf3eb8eb600c48ec34afc7

Name:           perl-File-Tail
Version:        1.3
Release:        34%{?dist}
Summary:        Perl extension for reading from continuously updated files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Tail
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/File-Tail-%{version}.tar.gz
Patch0:         File-Tail-1.3-init-objects.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes) >= 1.12
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Copy)
Requires:       perl(Time::HiRes) >= 1.12

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Time::HiRes\\)$

%description
The primary purpose of File::Tail is reading and analyzing log files
while they are being written, which is especially useful if you are
monitoring the logging process with a tool like Tobias Oetiker's MRTG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Tail-%{version}
%patch -P0 -p1 -b .fix

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Tail.3*

%changelog
%autochangelog
