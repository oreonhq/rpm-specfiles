%global source0_hash b9cbc4dcd8233e8d1d7f1481ddb79a4a5f9db7180cb3ef02b4bcbee05e65ea0c
Name:		perl-Hash-StoredIterator
Version:	0.008
Release:        1%{?dist}
Summary:        Functions for accessing a hash's internal iterator
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Hash-StoredIterator
Source0:        https://cpan.metacpan.org/modules/by-module/Hash/Hash-StoredIterator-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::Bundle::Extended)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
In perl all hashes have an internal iterator. This iterator is used by the
each() function, as well as by keys() and values(). Because these all share use
of the same iterator, they tend to interact badly with each other when nested.

Hash::StoredIterator gives you access to get, set, and init the iterator inside
a hash. This allows you to store the current iterator, use each / keys / values
etc., and then restore the iterator, which helps you to ensure you do not
interact badly with other users of the iterator.

Along with low-level get / set / init functions, there are also 2 variations of
each() that let you act upon each key/value pair in a safer way than vanilla
each().

This module can also export new implementations of keys() and values() that
stash and restore the iterator so that they are safe to use within each().

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-StoredIterator-%{version}

%build

perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
