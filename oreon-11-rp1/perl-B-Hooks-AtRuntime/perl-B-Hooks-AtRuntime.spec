%global source0_hash ca7f8231e48c0477f688287fd0b211fc98ed4668fa4fb7133b1a8d75e92c4132
Name:           perl-B-Hooks-AtRuntime
Version:        8
Release:        1%{?dist}
Summary:        Lower blocks from compile time to runtime
License:        BSD-2-Clause
URL:            https://metacpan.org/dist/B-Hooks-AtRuntime/
Source0:        https://cpan.metacpan.org/authors/id/B/BM/BMORROW/B-Hooks-AtRuntime-%{version}.tar.gz
Recommends:     perl(Filter::Util::Call)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Exports)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module allows code that runs at compile-time to do something at
runtime. A block passed to at_runtime gets compiled into the code that's
currently compiling, and will be called when control reaches that point
at runtime. In the example in the SYNOPSIS, the warnings will occur in
order, and if that section of code runs more than once, so will all
three warnings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Hooks-AtRuntime-%{version}

%build

%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
