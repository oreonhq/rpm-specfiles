%global source0_hash 3d61d07ef43b0126f5b4de4f415a256fa859fa88dc4fdabaad70b7be7c682cf0
Name:           perl-XML-SAX-Writer
Version:        0.57
Release:        1%{?dist}
Summary:        SAX2 Writer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-SAX-Writer
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-SAX-Writer-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(XML::SAX::Writer)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A new XML Writer to match the SAX2 effort.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-SAX-Writer-%{version}
find -type f -exec chmod -x {} +

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.57-25
- Prepare for Oreon 11 (RP1)
