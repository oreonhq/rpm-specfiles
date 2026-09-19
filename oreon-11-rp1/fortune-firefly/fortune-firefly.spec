%global source0_hash none

Name:		fortune-firefly
Version:	2.1.2
Release:        39%{?dist}
Summary:	Quotes from the TV series "Firefly"

# No version specified, only attribution is spec file, but maintainer is upstream.
License:	GPL-1.0-or-later
URL:		http://www.daughtersoftiresias.org/progs/firefly/
#Source0:	http://www.daughtersoftiresias.org/progs/firefly/%{name}-%{version}.tar.bz2
Source1:	http://www.daughtersoftiresias.org/progs/firefly/fortune-firefly-%{version}/firefly
Source2:	http://www.daughtersoftiresias.org/progs/firefly/fortune-firefly-%{version}/README
BuildArch:	noarch
BuildRequires:	%{_bindir}/strfile

Requires:	fortune-mod

%description
Fortune-firefly provides a set of quotes from the popular television series
"Firefly", and its movie "Serenity", by Joss Whedon.  

Quote authors include Tim Minear, Joss Whedon, Ben Edulund, Jane Esperson,
Drew Z. Greenberg, Jose Molina, Cheryl Cain, and Brent Matthews.

%prep
%setup -T -c
cp %{SOURCE1} ./firefly
cp %{SOURCE2} ./README

%build
# generate the firefly.dat file
%{_bindir}/strfile firefly

%install
rm -rf $RPM_BUILD_ROOT
install -d m755 $RPM_BUILD_ROOT%{_datadir}/games/fortune
install -m644 firefly $RPM_BUILD_ROOT%{_datadir}/games/fortune/
install -m644 firefly.dat $RPM_BUILD_ROOT%{_datadir}/games/fortune/

%files
%doc README
%{_datadir}/games/fortune/firefly
%{_datadir}/games/fortune/firefly.dat

%changelog
%autochangelog
