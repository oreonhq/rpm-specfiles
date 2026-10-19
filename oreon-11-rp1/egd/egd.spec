%global source0_hash 8d707439a118695b269b3c7b9a106fe6cc0eaab6bc17fc9e6ad359f282310d69
Name:		egd
Summary:        Entropy Gathering Daemon
Version:	0.9
Release:        1%{?dist}
License:	GPL-1.0-or-later OR LicenseRef-Callaway-MIT
Source0:        http://download.sourceforge.net/egd/%{name}-%{version}.tar.gz
URL:		http://egd.sourceforge.net/
Patch0:         egd-0.9-ip-neigh.patch
BuildArch:	noarch
Requires:	procps, iproute, coreutils, util-linux, tcpdump
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl-generators
# /oreon:deps
%description
EGD is an Entropy Gathering Daemon meant to be used on systems that can run GPG 
but which don't have a convenient (or reliable) source of random bits. It is a 
regular user-space program that sits around, running programs like 'w' and 
'last' and 'vmstat', collecting the randomness (or at least the 
unpredictability) inherent in the output of these system statistics programs 
when used on a reasonably busy system. It slowly stirs the output of these 
gathering programs into a pool of entropy, much like the linux kernel device, 
and allows other programs to read out random bits from this pool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .neigh

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
