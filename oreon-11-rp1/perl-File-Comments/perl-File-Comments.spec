%global source0_hash 5f848ca06f9f9d95d5ba63f5e6847806d794ea266ea6cb7c9a6931bcf14c1390

Summary:	Recognizes file formats and extracts format-specific comments
Name:		perl-File-Comments
Version:	0.08
Release:	44%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Url:		https://metacpan.org/release/File-Comments
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-Comments-%{version}.tar.gz
Patch0:		File-Comments-0.08-provides.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(HTML::TokeParser) >= 2.28
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(Log::Log4perl) >= 0.50
BuildRequires:	perl(Module::Pluggable) >= 2.4
BuildRequires:	perl(Pod::Parser) >= 1.14
BuildRequires:	perl(PPI) >= 1.115
BuildRequires:	perl(strict)
BuildRequires:	perl(Sysadm::Install) >= 0.11
BuildRequires:	perl(warnings)
# Examples
BuildRequires:	perl(Getopt::Std)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(Pod::Parser) >= 1.14
Requires:	perl(PPI) >= 1.115

%description
File::Comments guesses the type of a given file, determines the format
used for comments, extracts all comments, and returns them as a
reference to an array of chunks. Alternatively, it strips all comments
from a file.

Currently supported are Perl scripts, C/C++ programs, Java, makefiles,
JavaScript, Python and PHP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Comments-%{version}

# Note: not turning off exec bits in examples because they don't
# introduce any unwanted dependencies (nor any dependencies that
# are not satisfied by packages that are already required)

# Remove provide for local package not in regular search path
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test TEST_VERBOSE=1

%files
%doc Changes README eg/
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Comments.3*
%{_mandir}/man3/File::Comments::Plugin.3*
%{_mandir}/man3/File::Comments::Plugin::C.3*
%{_mandir}/man3/File::Comments::Plugin::HTML.3*
%{_mandir}/man3/File::Comments::Plugin::Java.3*
%{_mandir}/man3/File::Comments::Plugin::JavaScript.3*
%{_mandir}/man3/File::Comments::Plugin::Makefile.3*
%{_mandir}/man3/File::Comments::Plugin::PHP.3*
%{_mandir}/man3/File::Comments::Plugin::Perl.3*
%{_mandir}/man3/File::Comments::Plugin::Python.3*
%{_mandir}/man3/File::Comments::Plugin::Shell.3*

%changelog
%autochangelog
