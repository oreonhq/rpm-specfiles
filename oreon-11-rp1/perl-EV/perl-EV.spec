%global source0_hash 18bb66df4932ea61471dfb6057b5b27944f32d5be31fca832030a0c8082422a5

Name:           perl-EV
Version:        4.37
Release:        1%{?dist}
Summary:        Wrapper for the libev high-performance event loop library

# Note: The source archive includes a libev/ folder which contents are licensed
#       as "BSD or GPLv2+". However, those are removed at build-time and
#       perl-EV is instead built against the system-provided libev.
License:        GPL-1.0-or-later
URL:            https://metacpan.org/release/EV
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/EV-%{version}.tar.gz
Patch0:         perl-EV-4.03-Don-t-ask-questions-at-build-time.patch
Patch1:         perl-EV-4.30-Don-t-check-bundled-libev.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(common::sense)
BuildRequires:  gdbm-devel
BuildRequires:  libev-source >= 4.33
BuildRequires:  perl(AnyEvent) => 2.6
BuildRequires:  perl(Canary::Stability)

# We remove the upstream bundled libev, but still build against statically
# linked files from the libev-source package.
Provides:       bundled(libev)

%{?perl_default_filter}


Provides:       perl(EV)
Provides:       perl(EV::MakeMaker)
%description
This module provides an interface to libev
(<http://software.schmorp.de/pkg/libev.html>). While the included documentation
is comprehensive, one might also consult the documentation of libev itself
(<http://cvs.schmorp.de/libev/ev.html>) for more subtle details on watcher
semantics or some discussion on the available backends, or how to force a
specific backend with "LIBEV_FLAGS", or just about in any case because it has
much more detailed information.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n EV-%{version}

%patch -P0 -p1
%patch -P1 -p0

# remove all traces of the bundled libev
rm -fr ./libev

# use the sources from the system libev
mkdir -p ./libev
cp -r /usr/share/libev-source/* ./libev/


%build
PERL_CANARY_STABILITY_NOPROMPT=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
%make_build test


%files
%license COPYING
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/EV*.3pm*


%changelog
%autochangelog
