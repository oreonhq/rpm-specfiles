%global source0_hash c741339b43beb5eccaf21bb2c541c359860d51ee936d608bb4de773c0ed1c319
%global         forgeurl https://gitlab.cern.ch/curios/edg-mkgridmap
Name:		edg-mkgridmap
Version:	4.0.6
%global         tag v%{version}
%forgemeta
Release:        1%{?dist}
Summary:        A tool to build the grid map-file from VO servers
License:	Apache-2.0
Url:		%forgeurl
Source0:        %{forgeurl}/-/archive/%{tag}/%{name}-%{tag}.tar.bz2
Source1:        edg-mkgridmap.conf
Source2:        edg-mkgridmap.service
Source3:        edg-mkgridmap.timer
Patch0:         sbin-bin.patch
BuildArch:	noarch
Requires:	perl(URI)
Requires:	perl(Net::LDAP)
Requires:	perl(Net::LDAPS)
Requires:	perl(Term::ReadKey)
Requires:	perl(IO::Socket::SSL) >= 0.90
Requires:	perl(Net::SSLeay) >= 1.16
Requires:	perl(LWP)
Requires:	perl(XML::DOM)
Requires:	perl(Date::Manip)
Requires:       perl(LWP::Protocol::https)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
edg-mkgridmap is a tool to build the grid map-file from VO servers,
taking into account both VO and local policies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%patch -P 0 -p 1

cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .

%build

%install
make install prefix=%{buildroot}
mkdir %{buildroot}%{_sysconfdir}
install -p -m 0600 edg-mkgridmap.conf %{buildroot}%{_sysconfdir}/edg-mkgridmap.conf
mkdir %{buildroot}%{_sysconfdir}/grid-security
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 edg-mkgridmap.service %{buildroot}%{_unitdir}/edg-mkgridmap.service
install -p -m 0644 edg-mkgridmap.timer   %{buildroot}%{_unitdir}/edg-mkgridmap.timer
%oreon_autofiles main

%post

%systemd_post edg-mkgridmap.service edg-mkgridmap.timer
%preun

%systemd_preun edg-mkgridmap.service edg-mkgridmap.timer
%postun

%systemd_postun_with_restart edg-mkgridmap.service edg-mkgridmap.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
