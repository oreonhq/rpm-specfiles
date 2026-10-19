%global source2_hash 300885f9bf7de30e7256dac8b6327d3ad047aeb46d0ba5ba10ac0500f3d18073
%global source1_hash 470d2a69a6d97559bba4193545d12c02b5539b542dcbf8f616a5d271924a2927
%global source0_hash 34962bb554be726e6a852fbc04fd56123f69f9dd6f48cee8e25eb5a1a42f4e05
Summary:        Macros for aclocal to install configuration files
Summary(pl):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.22
Release:        1%{?dist}
License:	LicenseRef-Callaway-GPLv3-with-exceptions
Source0:        https://downloads.sourceforge.net/project/courier/sysconftool/%{version}/%{name}-%{version}.tar.bz2
Source1:	https://downloads.sourceforge.net/project/courier/sysconftool/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:	https://www.courier-mta.org/KEYS.bin
URL:		https://www.courier-mta.org/sysconftool/
BuildArch:	noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl
sysconftool jest narzędziem, które pomaga instalować pliki
konfiguracyjne aplikacji. sysconftool pozwala na wymienienie
istniejących aplikacji na nowsze wersje bez straty starszych wersji
plików konfiguracyjnych.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build

autoreconf -fiv
%configure
%make_build
%install
%make_install
ln -sf ../share/sysconftool/sysconftoolcheck %{buildroot}%{_bindir}/
ln -sf ../share/sysconftool/sysconftoolize.pl %{buildroot}%{_bindir}/sysconftoolize
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
