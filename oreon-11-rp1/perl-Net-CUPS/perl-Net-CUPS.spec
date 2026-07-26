%global source0_hash d7bc77ff0f62bf874c843c590eb12a80bbd44749a2fb74dbed445c35d0e85a85

Name:           perl-Net-CUPS
Version:        0.64
Release:        32%{?dist}
Summary:        Perl bindings to the CUPS C API Interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-CUPS
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NINE/Net-CUPS-%{version}.tar.gz
Patch0:         perl-Net-CUPS-use-libcupsfilters.patch
BuildRequires:  coreutils
BuildRequires:  cups-devel
BuildRequires:  libcupsfilters-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Net::CUPS is an interface to the Common Unix Printing System API.  If you feel
an urge to control CUPS servers via Perl, this is a good way to do it :)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-CUPS-%{version}
%patch -P0 -p1 -b .libcupsfilters
find . -type f -exec chmod -c -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
%autochangelog
