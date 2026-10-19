%global source0_hash 3df69e23d8b34ee7fac981efd1cc56f173c9eef6dffe3ba19ae8b3772e24ec85
Summary:        Converter between the rpm, dpkg, stampede slp, and Slackware tgz file formats
Name:           alien
Version:        8.95.9
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://sourceforge.net/projects/alien-pkg-convert/
Source0:        http://downloads.sourceforge.net/alien-pkg-convert/%{name}_%{version}.tar.xz
Requires:       dpkg, debhelper, rpm-build
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
# /oreon:deps
%description
Alien is a program that converts between the rpm, dpkg, stampede 
slp, and Slackware tgz file formats. If you want to use a package 
from another distribution than the one you have installed on your 
system, you can use alien to convert it to your preferred package 
format and install it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor VARPREFIX=%{buildroot}
make
%install
make pure_install DESTDIR=%{buildroot} \
        VARPREFIX=%{buildroot} \
        PREFIX=%{buildroot}%{_prefix}
%{__rm} -rf %{buildroot}%{perl_vendorarch}/auto/Alien
chmod 755 %{buildroot}%{_bindir}/alien
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
