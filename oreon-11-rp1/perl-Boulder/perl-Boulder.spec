%global source0_hash 5e2b3300384b2b229adb4f67179a120d236948080100462ed7e12fbda25f041b

Name:           perl-Boulder
Version:        1.30
Release:        54%{?dist}
Summary:        An API for hierarchical tag/value structures
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Boulder
Source0:        https://cpan.metacpan.org/modules/by-module/Boulder/Boulder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  sed
# Run-time:
# Bio::Seq is optional
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(constant)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::Parser)
# Tests:
BuildRequires:  perl(lib)

%description
Boulder provides a simple stream-oriented format for transmitting data
objects between one or more processes.  It does not provide for the
serialization of Perl objects the way FreezeThaw or Data::Dumper do, but it
does provide the advantage of being language independent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Boulder-%{version}
#Uses a non-existent module
rm Boulder/Labbase.pm
sed -i -e '/^Boulder\/Labbase.pm/d' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

perldoc -t perlgpl > COPYING
perldoc -t perlartistic > Artistic

%check
make test

%files
%license COPYING Artistic
%doc ChangeLog README
%doc %{perl_vendorlib}/Boulder.pod
%{perl_vendorlib}/Boulder/
%{perl_vendorlib}/Stone*
%{_mandir}/man3/*

%changelog
%autochangelog
