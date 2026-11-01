%global source0_hash 2219a37cb3cd9ab5ae271c7a03c5dc0d2458ffb922f67def5b89a3a065662697
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: authselect
Version: 1.8.0
Release: 1%{?dist}
Summary: Configures authentication and identity sources
License: GPL-3.0-or-later
URL: https://github.com/authselect/authselect
Source0: https://github.com/authselect/authselect/archive/%{version}/authselect-%{version}.tar.gz
Provides: authselect-libs = %{version}-%{release}
Requires: pam

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: popt-devel
BuildRequires: libselinux-devel
BuildRequires: pkgconf

%description
authselect selects system identity and authentication sources from a set
of profiles and writes the PAM and nsswitch configuration.

%package devel
Summary: Development files for authselect
Requires: authselect%{?_isa} = %{version}-%{release}
Provides: pkgconfig(authselect)

%description devel
Headers and libraries for developing against authselect.

%prep
%oreon_sha256
%autosetup -n authselect-%{version} -p1

%build
autoreconf -fi
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING
%dir %{_sysconfdir}/authselect
%dir %{_sysconfdir}/authselect/custom

%files devel -f %{_builddir}/%{name}-devel.files
