%global source0_hash 53a0bdb2656891c508a470d93cb7e1cfeab38eea9e5829560a7d8b5f600f6bf2
Name:           perl-Term-Shell
Version:        0.13
Release:        1%{?dist}
Summary:        Simple command-line shell framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Shell
Source0:        https://cpan.metacpan.org/modules/by-module/Term/Term-Shell-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Temp)
Requires:       perl(Term::ReadKey)
Requires:       perl(Text::Autoformat)
Suggests:       perl(Term::InKey)
Suggests:       perl(Term::Screen)
Suggests:       perl(Term::Size)
Obsoletes:     perl-Term-Shell-tests < %{version}-%{release}
Provides:      perl-Term-Shell-tests = %{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Term::Shell lets you write simple command-line shells. All the boring
details like command-line parsing, terminal handling, and tab completion
are handled for you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Shell-%{version}

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
