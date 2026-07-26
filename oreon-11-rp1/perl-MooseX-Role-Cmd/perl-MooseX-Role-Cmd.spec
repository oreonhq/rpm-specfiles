%global source0_hash 3e13143b0e0d2000c4df53890e5ca086b50444f23d3e934a1a9555aee9cfe956

Name:           perl-MooseX-Role-Cmd
Version:        0.10
Release:        40%{?dist}
Summary:        Wrap system command binaries the Moose way
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Role-Cmd
Source0:        https://cpan.metacpan.org/authors/id/E/ED/EDENC/MooseX-Role-Cmd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(IPC::Cmd) >= 0.42
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose) >= 0.24
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
MooseX::Role::Cmd is a Moose role intended to ease the task of building
command-line wrapper modules. It automatically maps Moose objects into
command strings which are passed to IPC::Cmd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Role-Cmd-%{version}

# Unbundle modules
rm -rf inc
sed -i -e '/^inc$/d' MANIFEST

# Filter requires
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(MooseX::Role::Cmd::Meta::Attribute::Trait)/d'
EOF

%define __perl_requires %{_builddir}/MooseX-Role-Cmd-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
