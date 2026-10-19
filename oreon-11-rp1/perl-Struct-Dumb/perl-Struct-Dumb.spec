%global source0_hash ebc9032640777a5bf900a30de0e554356af9cd95101e512a34fe15535c682508
Name:           perl-Struct-Dumb
Version:        0.16
Release:        2%{?dist}
Summary:        Make simple lightweight record-like structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Struct-Dumb
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(experimental)
Requires:       perl(overload)
%{?perl_default_filter}
Provides:       perl(Struct::Dumb)
Provides:       perl(Struct::Dumb)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Struct::Dumb creates record-like structure types, similar to the struct
keyword in C, C++ or C#, or Record in Pascal. An invocation of this module
will create a construction function which returns new object references
with the given field values. These references all respond to lvalue methods
that access or modify the values stored.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Struct-Dumb-%{version}

%build

/usr/bin/perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
