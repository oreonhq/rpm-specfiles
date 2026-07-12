%global source0_hash 7afc7ca2b9502e440241938ad97a3e7ebd550180ebd6142e1db394186b268e77

# TODO: BR: perl(File::Spec::Link) when available

Name:		perl-Cwd-Guard
Version:	0.05
Release:	29%{?dist}
Summary:	Temporarily change the current directory
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Cwd-Guard
Source0:	https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cwd-Guard-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(utf8)
# Module Runtime
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(if)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Requires)
# Runtime

Provides:       perl(Cwd::Guard)
%description
Cwd::Guard can change the current directory (chdir) using a limited scope.

  use Cwd::Guard qw/cwd_guard/;
  use Cwd;
 
  my $dir = getcwd;
  MYBLOCK: {
    my $guard = cwd_guard('/tmp/xxxxx') or die
      "failed chdir: $Cwd::Guard::Error";
    ... # chdir to /tmp/xxxxx
  }
  ... # back to $dir

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Cwd-Guard-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Cwd/
%{_mandir}/man3/Cwd::Guard.3*

%changelog
%autochangelog
