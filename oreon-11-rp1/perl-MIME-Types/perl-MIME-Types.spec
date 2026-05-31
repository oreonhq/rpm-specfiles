%global source0_hash f31b1666bdf420b4b65c373ce0129ee349dd24bab4cd16c7f01b698fe450be6f

# No Mojolicious in EPEL
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global have_mojo 1
%else
%global have_mojo 0
%endif

# Run extra test
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_with perl_MIME_Types_enables_extra_test
%else
%bcond_without perl_MIME_Types_enables_extra_test
%endif

Name:           perl-MIME-Types
Version:        2.30
Release:        2%{?dist}
Summary:        MIME types module for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Types
Source0:        https://cpan.metacpan.org/modules/by-module/MIME/MIME-Types-%{version}.tar.gz



BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
%if %{have_mojo}
BuildRequires:  perl(Mojo::Base)
%endif
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(warnings)
%if %{with perl_MIME_Types_enables_extra_test}
# Extra Tests
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
# Dependencies
# (none)

%description
MIME types are used in many applications, for instance as part of e-mail
and HTTP traffic, to indicate the type of content that is transmitted.

Sometimes detailed knowledge about a mime-type is need; however, this
module only knows about the file-name extensions that relate to some
file-type.  It can also be used to produce the right format: types that
are not registered at IANA need to use 'x-' prefixes.

%if %{have_mojo}
%package -n perl-MojoX-MIME-Types

Summary:        MIME Types for Mojolicious
Requires:       perl-MIME-Types = %{version}-%{release}

%description -n perl-MojoX-MIME-Types
This module is a drop-in replacement for Mojolicious::Types, but with a more
correct handling plus a complete list of types... a huge list of types.

Some methods ignore information they receive: those parameters are accepted
for compatibility with the Mojolicious::Types interface, but should not
contain useful information.

%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n MIME-Types-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_MIME_Types_enables_extra_test}
make test TEST_FILES="xt/*.t"
%endif

%files
%doc ChangeLog README.md
%{perl_vendorlib}/MIME/
%{_mandir}/man3/MIME::Type.3*
%{_mandir}/man3/MIME::Types.3*

%if %{have_mojo}
%files -n perl-MojoX-MIME-Types
%{perl_vendorlib}/MojoX/
%{_mandir}/man3/MojoX::MIME::Types.3*
%else
%exclude %{perl_vendorlib}/MojoX/
%exclude %{_mandir}/man3/MojoX::MIME::Types.3*
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.30-2
- Import
