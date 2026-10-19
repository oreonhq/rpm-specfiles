%global source1_hash 27d00febf2df8f32a60fffb84af677150a268e8b6a394a74801d38ab29fa28cb
%global source0_hash c91363e4e07f3521a867f68db602c95b53dc167e4366ee7ff254252b4176c62f
Name:		kpcli	
Version:	4.1.3
Release:        3%{?dist}
Summary:        KeePass Command Line Interface (CLI) / interactive shell
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:	noarch
URL:		http://kpcli.sourceforge.net/	
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.pl
Source1:	http://downloads.sourceforge.net/project/%{name}/README.txt
Requires:	perl(Term::ReadLine)
Requires:	perl(Term::ReadLine::Gnu)
Requires:	perl(Capture::Tiny)
Requires:	perl(Digest::MD5)
Requires:	perl(XML::Parser)
Recommends:	perl(File::KDBX)
Suggests:	perl(Crypt::PWSafe3) 
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
KeePass Command Line Interface (CLI) / interactive shell. 
Use this program to access and manage your KeePass databases
from a Unix-like command line.  These formats are supported:

KDB   - The original KeePass format (*.kdb)
KDBX3 - The first KeePass XML format (*.kdbx v3)
KDBX4 - The second KeePass XML format (*.kdbx v4)

%prep

cp -p %{SOURCE0} %{_builddir}/
cp -p %{SOURCE1} %{_builddir}/

%build

%install
mkdir -p %{buildroot}%{_bindir}/
install -p -m0755 %{name}-%{version}.pl %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
