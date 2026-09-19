%global source0_hash b1378679df4485b4459f609a3304238b3e92d91e43744c47b70abbe690d883d5

Name:		icon-naming-utils
Version:	0.8.90
Release:	%autorelease
Summary: 	A script to handle icon names in desktop icon themes

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
BuildArch:	noarch
URL:		http://tango.freedesktop.org/Standard_Icon_Naming_Specification
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2

BuildRequires:	perl-generators
BuildRequires:	perl(XML::Simple)
BuildRequires:	automake
BuildRequires: make

Patch0:		icon-naming-utils-0.8.7-paths.patch

%description
A script for creating a symlink mapping for deprecated icon names to
the new Icon Naming Specification names, for desktop icon themes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .paths

%build
# the paths patch patches Makefile.am
autoreconf
%configure
make %{?_smp_mflags}

%install
%{make_install}

# hmm, it installs an -uninstalled.pc file ...
rm -f $RPM_BUILD_ROOT%{_datadir}/pkgconfig/icon-naming-utils-uninstalled.pc

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/icon-name-mapping
%{_datadir}/icon-naming-utils/
%{_datadir}/pkgconfig/icon-naming-utils.pc

%changelog
%autochangelog
