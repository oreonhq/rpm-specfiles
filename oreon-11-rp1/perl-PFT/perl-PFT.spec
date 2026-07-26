%global source0_hash 81ca4d0c67263afd428b52ea654b1627fabf92508d13a1166ff857957f34d612

%global module PFT
Name:           perl-%{module}
Version:        1.4.1
Release:        18%{?dist}
Summary:        Hacker friendly static blog generator, core library

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/dacav/%{module}
Source0:        https://github.com/dacav/%{module}/archive/v%{version}.tar.gz#/%{module}-%{version}.tar.gz
BuildArch:      noarch

# As by /etc/rpmdevtools/spectemplate-perl.spec
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Additional dependencies at build time
# tangerine -c Makefile.PL lib \|
#       perl -nE '/^\s/ and next; s/^/BuildRequires:  perl(/; s/$/)/; print'
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::Tiny)

# As by /etc/rpmdevtools/spectemplate-perl.spec

%{?perl_default_filter}

%description
PFT stands for *Plain F. Text*, where the meaning of *F.* is up to
personal interpretation. Like *Fancy* or *Fantastic*.

It is yet another static website generator. This means your content is
compiled once and the result can be served by a simple HTTP server,
without need of server-side dynamic content generation.

This package provides the core library which abstracts away the file-system
access.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*

%check
LC_ALL=C.UTF-8 make test

%files
%doc %{_mandir}/man3/* 
%{!?_licensedir:%global license %%doc}
%{perl_vendorlib}/*
%doc README.md
%license LICENSE

%changelog
%autochangelog
