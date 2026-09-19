%global source0_hash 7dca0389e22e90ec1b1c199a29838803a1ae9ab34c086a926379b79edb069d89

Name:           whatmask
Version:        1.2
Release:        38%{?dist}
Summary:        Convert between different netmask types and show information

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.laffeycomputer.com/whatmask.html
Source0:        http://downloads.laffeycomputer.com/current_builds/whatmask/whatmask-1.2.tar.gz
Patch0:         whatmask-1.2-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc

%description
Whatmask is a small program that can analyze CIDR, netmask, netmask (hex), 
and wildcard bit notations to give useful information about a given network
block in question. It is similar to ipcalc, but provides an easier-to-use
interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure
make %{?_smp_mflags}
chmod 644 COPYING

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README

%{_bindir}/whatmask
%{_mandir}/man1/*

%changelog
%autochangelog
