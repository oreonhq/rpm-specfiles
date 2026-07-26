%global source0_hash 065a8e8a83bc4c2e52ae216aa6946fd8f5bab12bd61295db8dab1f12c825ed2f

Name:           jetring
Version:        0.32
Release:        4%{?dist}
Summary:        GPG keyring maintenance using changesets

License:        GPL-2.0-or-later
URL:            http://joeyh.name/code/jetring/
Source0:        http://ftp.debian.org/debian/pool/main/j/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  gnupg
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires: make
Requires:       gnupg

%description
jetring is a collection of tools that allow for GPG keyrings to be maintained
using changesets. It was developed with the Debian keyring in mind, and aims to
solve the problem that a GPG keyring is a binary blob that's hard for multiple
people to collaboratively edit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%make_build

%install
%make_install
install -Dpm 0644 jetring.7 %{buildroot}%{_mandir}/man7/jetring.7
install -d %{buildroot}%{_mandir}/man1
install -pm 0644 jetring-*.1 %{buildroot}%{_mandir}/man1

%files
%doc README
%license GPL
%{_bindir}/jetring*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
%autochangelog
