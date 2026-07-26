%global source0_hash 70e8af4aa21d19bab5edd9f43a6b3d6277748a65145d46ff0ea2ae4c59495c72

Name:           perl-IO-Socket-Multicast
Summary:        Perl library for sending and receiving multicast messages
Version:        1.12
Release:        33%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Socket-Multicast
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-%{version}.tar.gz
# The following license text is included due to the "perl" license assignment
# shown in Makefile.PL
Source1:        http://dev.perl.org/licenses/#/%{name}-Licensing.html

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Config)
BuildRequires:  findutils

# Needed during build for the perl test
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(IO::Interface) >= 0.94

Requires:       perl(IO::Interface) >= 0.94

%description
The IO::Socket::Multicast module sub-classes IO::Socket::INET to enable you
to manipulate multicast groups. With this module (and an operating system
that supports multicast), you will be able to receive incoming multicast
transmissions and generate your own outgoing multicast packets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n IO-Socket-Multicast-%{version}
cp -a %{SOURCE1} Licensing.html
chmod 644 examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete
find %{buildroot} -type d -empty -delete

%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%license Licensing.html
%doc Changes README examples/
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/*

%changelog
%autochangelog
