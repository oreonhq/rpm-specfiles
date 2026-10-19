%global source0_hash 09092a5955580e4aca3f83f48ff7f4395dd7dc69d0274e300f5393755d0e994b
Name: setuptool
Version: 1.19.11
Release:        1%{?dist}
Summary:        A text mode system configuration tool
License: GPL-2.0-or-later
Url: http://git.fedorahosted.org/git/?p=setuptool.git
Source0:        setuptool-%{version}.tar.gz
Requires: usermode
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  newt-devel
BuildRequires:  perl-XML-Parser
# /oreon:deps
%description
Setuptool is a user-friendly text mode menu utility which allows you
to access all of the text mode configuration programs included in the
operating system distribution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang setup
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
