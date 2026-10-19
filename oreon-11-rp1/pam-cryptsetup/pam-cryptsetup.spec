%global source0_hash b647a91224899c0f15a1919cb71c59aacb871e2001797e0181934bdb273a1846
%global commit 7b42892ea42cd710eab962236b3dd0ac55fbb402
%global shortcommit 7b42892
%global snapshot_date 20190823
%global snapinfo %{snapshot_date}.%{shortcommit}
Name:           pam-cryptsetup
Version:        0.1
Release:        1%{?dist}
Summary:        PAM module for updating LUKS-encrypted volumes
License:        Apache-2.0
URL:            https://github.com/google/pam-cryptsetup/
Source0:        https://github.com/google/%{name}//archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         %{name}-0.1-fix-stringop-truncation.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cryptsetup-devel
BuildRequires:  device-mapper-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
pam-cryptsetup provides a PAM module that allows LUKS-based disk encryption
passwords to be kept in sync with account passwords automatically based on
factors like if the user has decrypted the disk successfully previously.

The project as a whole consists of two parts: a PAM module pam_cryptsetup.so for
triggering on user authentication, and a helper program pam_cryptsetup_helper to
perform the actual encryption checks and modifications required.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

%build

./autogen.sh
%configure
sed -i 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' libtool
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/security/pam_cryptsetup.la
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
