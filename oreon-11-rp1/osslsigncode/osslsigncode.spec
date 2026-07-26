%global source0_hash 6c0a2ac937d4c5a49afcba107a8d97622aa84b6ac1508df913fe6e3d4831d82e

%if 0%{?rhel}
%bcond_with tests
%else
%ifarch s390x
%bcond_with tests
%else
# Disable tests since 2.3 version due
# https://github.com/mtrojnar/osslsigncode/issues/140#issuecomment-1060636197
%bcond_with tests
%endif
%endif

%global forgeurl https://github.com/mtrojnar/osslsigncode
%global tag %{version}

Name:       osslsigncode
Version:    2.12
%forgemeta
Release:    %autorelease
Summary:    OpenSSL-based Authenticode signing for PE, CAB, CAT, MSI, APPX

License:    GPL-3.0-or-later
URL:        %{forgeurl}
Source0:    %{forgesource}

# To prevent network access during tests
%dnl Patch:      %{name}-preventnetwork-access-during-tests.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   i686

BuildRequires: cmake >= 3.17
BuildRequires: coreutils
BuildRequires: gcc
%if 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine >= 3.0.0
%endif
BuildRequires: sed
BuildRequires: pkgconfig(libcrypto) >= 1.1.0
BuildRequires: pkgconfig(libcurl) >= 7.12.0
BuildRequires: pkgconfig(openssl) >= 3.0.0
BuildRequires: pkgconfig(zlib)
%if %{with tests}
BuildRequires: gcab
BuildRequires: java-1.8.0-openjdk-headless
BuildRequires: libfaketime
BuildRequires: mingw64-gcc
BuildRequires: msitools
BuildRequires: openssl >= 1.1.0
BuildRequires: vim-common
%endif

%description
osslsigncode is a small tool that implements part of the functionality of the
Microsoft tool signtool.exe - more exactly the Authenticode signing and
timestamping. But osslsigncode is based on OpenSSL and cURL, and thus should be
able to compile on most platforms where these exist.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
# https://bugzilla.redhat.com/show_bug.cgi?id=1882547#c2
%if %{with tests}
%ctest
%endif

%files
%license LICENSE.txt COPYING.txt
%doc README.md NEWS.md TODO.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/*.bash
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions

%changelog
%autochangelog
