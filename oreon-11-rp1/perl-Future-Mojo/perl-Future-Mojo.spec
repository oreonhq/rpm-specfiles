%global source0_hash 9e88a11e04ea4a65717afe63ae155630d2f8d3cf8d714f89348cb05c6edf5d1e
Name:           perl-Future-Mojo
Version:        1.003
Release:        5%{?dist}
Summary:        Use Future with Mojo::IOLoop
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Future-Mojo
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Future-Mojo-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Future) >= 0.49
Requires:       perl(Mojolicious) >= 7.54
Requires:       perl(Role::Tiny) >= 2.000002
%global __requires_exclude ^perl\\((Future|Mojolicious|Role::Tiny)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Loop::Mojo)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This subclass of Future stores a reference to the associated Mojo::IOLoop
instance, allowing the await method to block until the Future is ready.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Future-Mojo-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
