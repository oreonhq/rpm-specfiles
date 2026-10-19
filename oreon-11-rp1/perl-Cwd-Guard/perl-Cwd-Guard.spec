%global source0_hash 7afc7ca2b9502e440241938ad97a3e7ebd550180ebd6142e1db394186b268e77
Name:		perl-Cwd-Guard
Version:	0.05
Release:        29%{?dist}
Summary:        Temporarily change the current directory
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Cwd-Guard
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cwd-Guard-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Cwd::Guard)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
