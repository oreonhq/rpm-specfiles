%global source0_hash c4306a0f9bddb1ad6ed7850af40126402a1a8474a607c3586c47f450df65b0ce
Name:           ldapdiff
Version:        1.4.1
Release:        1%{?dist}
Summary:        Tool for incremental LDAP directory updates based on ldif files
License:        GPL-3.0-or-later
URL:            https://launchpad.net/ldapdiff
Source0:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}_src.tgz
Patch0:         ldapdiff-1.4.1-format-security.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openldap-devel
# /oreon:deps
%description
ldapdiff combines "diff" and "patch" functionality in one application.
The difference is, that ldapdiff is not designed for use on flat ascii
files, it is designed for "patching" ldap directories using ldif files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .fs
make clean

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
