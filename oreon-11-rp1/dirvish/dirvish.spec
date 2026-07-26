%global source0_hash e0807d77bd073142d459f9d41e2721e7e37e3fb676fc4300d65c878a1428c059

Name:           dirvish
Version:        1.2.1
Release:        36%{?dist}
Summary:        Fast, disk based, rotating network backup system

License:        OSL-2.0
URL:            http://www.dirvish.org/
Source0:        http://www.dirvish.org/dirvish-%{version}.tgz
# converts the installer to work in unattended mode
Patch0:         dirvish-1.2.1-install.patch
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       rsync

%description
Dirvish is a fast, disk based, rotating network backup system. With dirvish you
can maintain a set of complete images of your filesystems with unattended
creation and expiration. A dirvish backup vault is like a time machine for your
data. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/dirvish
PREFIX=$RPM_BUILD_ROOT%{_prefix} ./install.sh

%files
%dir %{_sysconfdir}/dirvish
%{_bindir}/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%doc CHANGELOG FAQ.html RELEASE.html TODO.html COPYING

%changelog
%autochangelog
