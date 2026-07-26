%global source0_hash a7268e49773a2c367ec9a0d268b15a57073c4b98f7d7a1be93400d663de35044

Name:           perl-Getopt-GUI-Long
Version:        0.93
Release:        33%{?dist}
Summary:        Wrapper around Getopt::Long to provide a GUI to applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Getopt-GUI-Long
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HARDAKER/Getopt-GUI-Long-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# QWizard modules are technically optional, but without them this package does
# not make much sense.
Requires:       perl(QWizard)
Requires:       perl(QWizard::Plugins::Bookmarks)
Requires:       perl(QWizard::Storage::File)

%description
This module is a wrapper around Getopt::Long that extends the value of
the original Getopt::Long module to:

1) add a simple graphical user interface option screen if no arguments
   are passed to the program.  Thus, the arguments to actually use are
   built based on the results of the user interface. If arguments were
   passed to the program, the user interface is not shown and the
   program executes as it normally would and acts just as if
   Getopt::Long::GetOptions had been called instead.  This requires
   the QWizard and Gtk2 or Tk interfaces to be installed too.

2) provide an auto-help mechanism such that -h and --help are
   handled automatically.  In fact, calling your program with -h
   will default to showing the user a list of short-style arguments
   when one exists for the option.  Similarly --help will show the
   user a list of long-style when possible.  --help-full will list
   all potential arguments for an option (short and long both).

It's designed to make the creation of graphical shells trivial
without the programmer having to think about it much as well as
providing automatic good-looking usage output without the
programmer needing to write usage() functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Getopt-GUI-Long-%{version}
# rpm doc examples shouldn't be executable
chmod a-x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%files
%doc examples README
%dir %{perl_vendorlib}/Getopt
%dir %{perl_vendorlib}/Getopt/GUI
%{perl_vendorlib}/Getopt/GUI/Long.pm
%{_mandir}/man3/Getopt::GUI::Long.*

%changelog
%autochangelog
