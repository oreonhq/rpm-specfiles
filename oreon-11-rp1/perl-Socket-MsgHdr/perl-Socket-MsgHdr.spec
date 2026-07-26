%global source0_hash 96501c15e3dee4d8288c1c68beed3a0a7b3d4704cc6e274f20162b60fb51783c

%{?perl_default_filter}
%global __requires_exclude MsgHdr.so

Name:           perl-Socket-MsgHdr
Version:        0.05
Release:        25%{?dist}
Summary:        Sendmsg, recvmsg and ancillary data operations
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Socket-MsgHdr
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FELIPE/Socket-MsgHdr-%{version}.tar.gz

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76

BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(bytes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)

%description
Socket::MsgHdr provides advanced socket messaging operations via sendmsg
and recvmsg. Like their C counterparts, these functions accept few
parameters, instead stuffing a lot of information into a complex structure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Socket-MsgHdr-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Socket*
%{_mandir}/man3/*

%changelog
%autochangelog
