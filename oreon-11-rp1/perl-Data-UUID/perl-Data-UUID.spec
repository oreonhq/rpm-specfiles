%global source0_hash 95bda7276265f57bc48ffdeddec5ef28cd6f765e3a183757fa5f09f0ce6b98ac

Name:		perl-Data-UUID
Version:	1.227
Release:	7%{?dist}
Summary:	Globally/Universally Unique Identifiers (GUIDs/UUIDs)
# Makefile.PL says BSD but LICENSE file is HP-1989
# LICENSE: HP-1989
# source/ptable.h: GPL-1.0-or-later OR Artistic-1.0-Perl
# Issue for license clarification
# https://github.com/bleargh45/Data-UUID/issues/26
License:	HP-1989 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:		https://metacpan.org/release/Data-UUID
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-UUID-%{version}.tar.gz



# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(blib)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Test::More)
BuildRequires:	perl(threads)
%if ! 0%{?_module_build}
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Pod::Coverage) >= 1.06
%endif
# Dependencies
# (none)

# Avoid provides for private shared objects
%{?perl_default_filter}

%description
This module provides a framework for generating v3 UUIDs (Universally Unique
Identifiers, also known as GUIDs (Globally Unique Identifiers). A UUID is 128
bits long, and is guaranteed to be different from all other UUIDs/GUIDs
generated until 3400 CE.

UUIDs were originally used in the Network Computing System (NCS) and later in
the Open Software Foundation's (OSF) Distributed Computing Environment.
Currently many different technologies rely on UUIDs to provide unique identity
for various software components. Microsoft COM/DCOM for instance, uses GUIDs
very extensively to uniquely identify classes, applications and components
across network-connected systems.

The algorithm for UUID generation, used by this extension, is described in the
Internet Draft "UUIDs and GUIDs" by Paul J. Leach and Rich Salz (see RFC 4122).
It provides a reasonably efficient and reliable framework for generating UUIDs
and supports fairly high allocation rates - 10 million per second per machine -
and therefore is suitable for identifying both extremely short-lived and very
persistent objects on a given system as well as across the network.

This module provides several methods to create a UUID. In all methods,
<namespace> is a UUID and <name> is a free form string.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Data-UUID-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test AUTHOR_TESTING=1
perl smp-test/collision.t

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/Data/
%{_mandir}/man3/Data::UUID.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.227-7
- Prepare for Oreon 11 (RP1)
