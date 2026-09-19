%global source0_hash de96dd6c7c1f25f3287aa7af64902bf84acaaa8e0c3bb76aa1676367e04a08b7

Name:           perl-X11-Protocol
Version:        0.56
Release:        50%{?dist}
Summary:        X11-Protocol - Raw interface to X Window System servers

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/X11-Protocol
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMCCAM/X11-Protocol-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(vars)
%if 0%{?_with_X:1}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif

%description
X11::Protocol is a client-side interface to the X11 Protocol (see X(1) for
information about X11), allowing perl programs to display windows and
graphics on X11 servers.

A full description of the protocol is beyond the scope of this documentation;
for complete information, see the I<X Window System Protocol, X Version 11>,
available as Postscript or *roff source from C<ftp://ftp.x.org>, or
I<Volume 0: X Protocol Reference Manual> of O'Reilly & Associates's series of
books about X (ISBN 1-56592-083-X, C<http://www.oreilly.com>), which contains
most of the same information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n X11-Protocol-%{version}

# Testing requires X - use "rpmbuild --with X"
%if 0%{!?_with_X:1}
perl -pi -e 'print "print \"Remaining tests require X\n\"; exit 0;" 
    if /Insert your test code below/;' test.pl 
%endif

/usr/bin/perldoc -t perlartistic > Artistic
/usr/bin/perldoc -t perlgpl > COPYING

# Remove shebangs from module code
find . -name '*.pm' -exec sed -i -e '/^#!\/usr\/bin\/perl$/d' {} ';'

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if 0%{?_with_X:1}
    xvfb-run -a make test
%else
    make test
%endif

#make test

%files
%license Artistic COPYING
%doc README Changes Todo eg
%{perl_vendorlib}/X11/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
