%global source0_hash b9f5387163e4947937a851eaa0c84e1d9973f5b17708753d967d00c3744291ec
Summary:        Run an entire GNOME session under valgrind
Name:		gnome-valgrind-session
Version:	1.1
Release:        36%{?dist}
License:	LicenseRef-Fedora-Public-Domain
URL:		http://hp.cl.no/proj/gnome-valgrind-session/
Source0:        http://hp.cl.no/proj/gnome-valgrind-session/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-desktop.patch
Patch1:		%{name}-%{version}-use-gnome-session-suffix-pid-drop-alignment.patch
Patch2:		%{name}-%{version}-add-xorg-label.patch
Requires:	gnome-session 
Requires:	valgrind
BuildArch:	noarch
# oreon:deps

# /oreon:deps
%description
GNOME Valgrind Session adds new types of GNOME session to the login manager's
session menu. These let you instrument your entire session with Valgrind for
debugging purposes. The generated logs are collected and subjected to simple
postprocessing when you log out. The result is saved to a file in your home
directory.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xsessions
install -p -m0755 gnome-valgrind-errors $RPM_BUILD_ROOT/%{_bindir}
install -p -m0755 gnome-valgrind-errors-postprocess $RPM_BUILD_ROOT/%{_bindir}
install -p -m0755 gnome-valgrind-leaks $RPM_BUILD_ROOT/%{_bindir}
install -p -m0755 gnome-valgrind-leaks-postprocess $RPM_BUILD_ROOT/%{_bindir}
install -p -m0644 gnome-valgrind-errors.desktop \
  $RPM_BUILD_ROOT/%{_datadir}/xsessions
install -p -m0644 gnome-valgrind-leaks.desktop \
  $RPM_BUILD_ROOT/%{_datadir}/xsessions
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
