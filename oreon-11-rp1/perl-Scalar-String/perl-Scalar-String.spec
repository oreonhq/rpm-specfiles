%global source0_hash f54a17c9b78713b02cc43adfadf60b49467e7634d31317e8b9e9e97c26d68b52
Name:           perl-Scalar-String
Version:        0.003
Release:        1%{?dist}
Summary:        String aspects of scalars
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scalar-String
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Scalar-String-%{version}.tar.gz
Requires:       perl(Carp)
Requires:       perl(XSLoader)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(bytes)
BuildRequires:  perl(if)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is about the string part of plain Perl scalars. A scalar has a
string value, which is notionally a sequence of Unicode codepoints, but
may be internally encoded in either ISO-8859-1 or UTF-8. In places, and
more so in older versions of Perl, the internal encoding shows through. To
fully understand Perl strings it is necessary to understand these
implementation details.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Scalar-String-%{version}
%oreon_prep
%build

%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
