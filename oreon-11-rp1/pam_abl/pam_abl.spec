%global source0_hash dff9437af247fee19e8269919a3eed44c1e69874c1fa06325997c8d1eeb7eeb4
Name:           pam_abl
Summary:        A Pluggable Authentication Module (PAM) for auto blacklisting
Version:        0.6.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://pam-abl.sourceforge.net/
Source0:        https://downloads.sourceforge.net/pam-abl/pam-abl-%{version}.tar.gz
Patch0:         pam_abl-0.6.0-whitelistroot.patch
Patch1:         pam_abl-0.6.0-Port-to-CMake-4.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  bash
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libdb-devel
BuildRequires:  pam-devel
# /oreon:deps
%description
Provides auto blacklisting of hosts and users responsible for repeated
failed authentication attempts. Generally configured so that
blacklisted users still see normal login prompts but are guaranteed to
fail to authenticate. A command line tool allows to query or purge the
databases used by the pam_abl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
cd doc
sh generate.sh
%install
%cmake_install
install -d -m 755 ${RPM_BUILD_ROOT}/%{_libdir}/security
%if %(test "%{_libdir}" != "/usr/lib" && echo 1 || echo 0)
  mv ${RPM_BUILD_ROOT}/usr/lib/security/pam_abl.so  ${RPM_BUILD_ROOT}/%{_libdir}/security/pam_abl.so 
%endif
install -D -m 644 conf/pam_abl.conf %{buildroot}%{_sysconfdir}/security/pam_abl.conf
install -d -m 755 %{buildroot}%{_localstatedir}/lib/abl
install -D -m 644 doc/pam_abl.1      %{buildroot}%{_mandir}/man1/pam_abl.1
install -D -m 644 doc/pam_abl.conf.5 %{buildroot}%{_mandir}/man5/pam_abl.conf.5
install -D -m 644 doc/pam_abl.8      %{buildroot}%{_mandir}/man8/pam_abl.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
