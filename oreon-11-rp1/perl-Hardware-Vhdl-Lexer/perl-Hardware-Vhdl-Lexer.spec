%global source0_hash d7ba36a9ea462e1acfddf2cb0531f225303a50dc0a144d06bd0130b23161e9c4

Name:           perl-Hardware-Vhdl-Lexer
Version:        1.00
Release:        49%{?dist}
Summary:        Split VHDL code into lexical tokens
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Hardware-Vhdl-Lexer
Source0:        https://cpan.metacpan.org/authors/id/M/MY/MYKL/Hardware-Vhdl-Lexer-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Std)
BuildRequires:  perl(Readonly) >= 1.03
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:       perl(Readonly) >= 1.03

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Readonly\\)$

%description
Hardware::Vhdl::Lexer splits VHDL code into lexical tokens. To use it, you
need to first create a lexer object, passing in something which will supply
chunks of VHDL code to the lexer. Repeated calls to the get_next_token
method of the lexer will then return VHDL tokens (in scalar context) or a
token type code and the token (in list context). get_next_token returns
undef when there are no more tokens to be read.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hardware-Vhdl-Lexer-%{version}

# rpmlint : line endings spurious-executable-perm
for i in Changes README lib/Hardware/Vhdl/Lexer.pm ; do
  echo "Fixing wrong-file-end-of-line-encoding : $i"
  %{__sed} 's/\r//' $i > $i.rpmlint
  touch -r $i $i.rpmlint;
  %{__mv} $i.rpmlint $i
  echo "Fixing perms : $i"
  chmod 0644 $i
done

# workaround for bug in rpmbuild
# disables the Requires of modules in commented code
%{__sed} "s|use regexp-generating|#use regexp-generating|" \
  lib/Hardware/Vhdl/Lexer.pm > Lexer.pm
touch -r lib/Hardware/Vhdl/Lexer.pm Lexer.pm;
%{__mv} Lexer.pm lib/Hardware/Vhdl/Lexer.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
