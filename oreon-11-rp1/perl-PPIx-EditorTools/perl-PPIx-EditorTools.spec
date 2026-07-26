%global source0_hash b20ad28b3cf7044854326987bbb5c0422079068ceb22cb599396f3b886c1186c

Name:           perl-PPIx-EditorTools
Version:        0.21
Release:        25%{?dist}
Summary:        Utility methods and base class for manipulating Perl via PPI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPIx-EditorTools
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/PPIx-EditorTools-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor) >= 1.02
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(PPI) >= 1.215
BuildRequires:  perl(PPI::Find)
BuildRequires:  perl(Try::Tiny)
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Most)
# Optional tests:
BuildRequires:  perl(Test::CPAN::Changes)
Requires:       perl(PPI) >= 1.215
Requires:       perl(PPI::Find)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::XSAccessor\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(PPI\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(PPI\\) >= 1.203$

%description
Base class and utility methods for manipulating Perl via PPI. Pulled out
from the Padre::Task::PPI code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PPIx-EditorTools-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
