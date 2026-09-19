%global source0_hash cdcbc2c1c93627fe9cbc2619a7a7b8e39db0c3cb41822c8ffba9b98cc09b9483

Name:           perl-Catalyst-Plugin-Session-Store-Delegate
Version:        0.06
Release:        41%{?dist}
Summary:        Delegate session storage to an application model object
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-Delegate
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-Store-Delegate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst::Model)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::Test::Store)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)

%{?perl_default_filter}

%description
This store plugins makes delegating session storage to a first class object
model easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-Store-Delegate-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
