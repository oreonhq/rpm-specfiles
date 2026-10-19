%global source0_hash ea88d58e251674fae39b49f4d3b5342eaccb8fcb55856cd304aa1a5ff3d41c92
Name:		perl-Regexp-Grammars
Version:	1.058
Release:        1%{?dist}
Summary:        Add grammatical parsing features to perl regular expressions
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Regexp-Grammars
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Regexp-Grammars-%{version}.tar.gz
BuildArch:	noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module adds a small number of new regular expressions constructs that
can be used to implement complete recursive-descent parsing.

These constructs use the grammar patterns that were added to perl's
regular expressions in perl 5.10.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Regexp-Grammars-%{version}

chmod -x Changes

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
