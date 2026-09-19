%global source0_hash c4306a0f9bddb1ad6ed7850af40126402a1a8474a607c3586c47f450df65b0ce

Name:           ldapdiff
Version:        1.4.1
Release:        %autorelease
Summary:        Tool for incremental LDAP directory updates based on ldif files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://launchpad.net/ldapdiff
Source0:        %{url}/trunk/%{version}/+download/ldapdiff-%{version}_src.tgz
Patch0:         ldapdiff-1.4.1-format-security.patch

BuildRequires:  gcc
BuildRequires:  openldap-devel
BuildRequires: make

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

%files
%doc AUTHORS ChangeLog debian/changelog TODO README
%{_bindir}/ldapdiff
%dir %{_datadir}/ldapdiff
%{_datadir}/ldapdiff/ldapdiff.conf.sample
%dir %{_datadir}/ldapdiff/samples
%{_datadir}/ldapdiff/samples/*
%{_mandir}/man1/ldapdiff.1.*

%changelog
%autochangelog
