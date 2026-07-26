%global source0_hash d0ee2d2588709f6554804a9c1ae2cad0feebe23bc237fb2ec25578ffc1618c07

Name:           perl-Inline-Python
Version:        0.58
Release:        2%{?dist}
Summary:        Write Perl subs and classes in Python
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-Python
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NINE/Inline-Python-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Inline) >= 0.46
BuildRequires:  perl(Inline::denter)
BuildRequires:  perl(JSON)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::ProcessTable) >= 0.53
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  python3
BuildRequires:  python3-devel
Requires:       perl(Inline) >= 0.46
Requires:       perl(Inline::denter)

# Remove underspecified generated dependency
%global __requires_exclude ^perl\\(Inline\\)$

%description
The Inline::Python module allows you to put Python source code directly
"inline" in a Perl script or module. It sets up an in-process Python
interpreter, runs your code, and then examines Python's symbol table for
things to bind to Perl. The process of interrogating the Python interpreter
for global variables only occurs the first time you run your Python code. The
name-space is cached, and subsequent calls use the cached version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Inline-Python-%{version}

%build
INLINE_PYTHON_EXECUTABLE=/usr/bin/python3 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README ToDo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Inline*
%{_mandir}/man3/*

%changelog
%autochangelog
