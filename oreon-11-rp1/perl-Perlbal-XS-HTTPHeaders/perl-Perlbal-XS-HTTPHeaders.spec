%global source0_hash 9cd6391c61a41b75790870776fb1a0b2487c34a16b9c96f2bd7caffe0e653aa3

%global libname Perlbal-XS-HTTPHeaders
Name:           perl-%{libname}
Version:        0.20
Release:        55%{?dist}
Summary:        Perlbal extension for processing HTTP headers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{libname}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{libname}-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Perlbal)
BuildRequires:  perl(Perlbal::HTTPHeaders)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module is used to read HTTP headers from a string and to parse them
into an internal storage format for easy access and modification. You can
also ask the module to reconstitute the headers into one big string, useful
if you're writing a proxy and need to read and write headers while
maintaining the ability to modify individual parts of the whole.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{libname}-%{version}
# Work around bug in EU::MM (RT#68613), remove forced CC options
sed -i -e "/CCFLAGS/d" Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Perlbal/XS
%{perl_vendorarch}/Perlbal/XS
%{_mandir}/man3/Perlbal::XS::HTTPHeaders.*

%changelog
%autochangelog
