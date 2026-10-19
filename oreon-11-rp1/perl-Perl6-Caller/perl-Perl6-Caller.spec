%global source0_hash be18c1a3f86f7881da560a87902810e7613fd5da128dad49e3cf7ed6e337daa3
Name:           perl-Perl6-Caller
Version:        0.100
Release:        1%{?dist}
Summary:        OO caller() interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl6-Caller
Source0:        https://cpan.metacpan.org/modules/by-module/Perl6/Perl6-Caller-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
By default, this module exports the caller function. This automatically
returns a new caller object. An optional argument specifies how many stack
frames back to skip, just like the CORE::caller function. This lets you do
things like this:

    print "In ",           caller->subroutine,
          " called from ", caller->filename,
          " line ",        caller->line;

If you do not wish the caller function imported, specify an empty import list
and instantiate a new Perl6::Caller object.

    use Perl6::Caller ();
    my $caller = Perl6::Caller->new;
    print $caller->line;

Note: if the results from the module seem strange, please read
perldoc -s caller carefully. It has stranger behavior than you might be aware.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl6-Caller-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
./Build test --test_files="xt/*.t"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
