%global source1_hash 6e903339fce488056ad7acfa2ab786a138a55580ea2a7604e4bc3acb5dd3ca1f
%global source0_hash ae4bf3b8f0a748f470531a650436b39182c8217ee9269a9c7e925c64380a9bda
%global source2_key_fpr 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D
Name:           uid_wrapper
Version:        1.3.2
Release:        1%{?dist}
Summary:        A wrapper for privilege separation
License:        GPL-3.0-or-later
Url:            http://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        uid_wrapper.keyring
Recommends:     cmake
Recommends:     pkgconfig
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
# /oreon:deps
%description
Some projects like a file server need privilege separation to be able to switch
to the connection user and do file operations. uid_wrapper convincingly lies
to the application letting it believe it is operating as root and even
switching between UIDs and GIDs as needed.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

This package doesn't have a devel package cause this project is for
development/testing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DUNIT_TESTING=ON
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-1
- Prepare for Oreon 11 (RP1)
