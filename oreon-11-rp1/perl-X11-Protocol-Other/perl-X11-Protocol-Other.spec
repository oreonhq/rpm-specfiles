%global source0_hash 3c625993dc7a8eb1d02e07108a666302459c6fc6f9f3d27615f7495158dc73f4

Name:           perl-X11-Protocol-Other
Version:        31
Release:        20%{?dist}
Summary:        Miscellaneous X11::Protocol helpers
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/X11-Protocol-Other
Source0:        https://cpan.metacpan.org/modules/by-module/X11/X11-Protocol-Other-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode) >= 1
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::HanExtra) >= 0.06
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(X11::Protocol)
# Tests
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)

%description
These are some helper functions for X11::Protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n X11-Protocol-Other-%{version}
chmod a-x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
