%global source0_hash fc64654f7d8da7071760ea0116e112b6d661b0a7bc3188dff1b2d52fb6a663cb

Name:           perl-Text-Format
Version:        0.63
Release:        4%{?dist}
Summary:        Various subroutines to format text

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Format
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Format-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests - not execute
# BuildRequires:  perl(Pod::Coverage::TrustPod)
# BuildRequires:  perl(Test::Code::TidyAll) >= 0.24
# BuildRequires:  perl(Test::CPAN::Changes)
# BuildRequires:  perl(Test::EOL)
# BuildRequires:  perl(Test::NoTabs)
# BuildRequires:  perl(Test::Pod) >= 1.41
# BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# BuildRequires:  perl(Test::TrailingSpace)

%description
The format routine will format under all circumstances even if the width isn't
enough to contain the longest words. Text::Wrap will die under these
circumstances, although I am told this is fixed. If columns is set to a small
number and words are longer than that and the leading 'whitespace' than there
will be a single word on each line. This will let you make a simple word list
which could be indented or right aligned. There is a chance for croaking if you
try to subvert the module. If you don't pass in text then the internal text is
worked on, though not modified. Text::Format is meant for more powerful text
formatting than Text::Wrap allows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Format-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/Text::Format.3*

%changelog
%autochangelog
