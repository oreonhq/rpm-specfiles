%global source0_hash 2352c2101d4f334e98e0d6d82c3f08f6902101bf812c1be89eb65ad9e9e30b48

Name:           whereami
Version:        1.0
Release:        31%{?dist}
Summary:        Displays work location

License:        GPL-3.0-or-later
URL:            http://pjp.dgplug.org/tools
Source:         %{url}/%{name}-%{version}.tar.gz
Patch:          pointer-decl.patch

BuildRequires:  gcc
BuildRequires:  make

%description
Whereami displays information about the machine(location) you are working on.
Information like terminal name, present working directory, host name, and the
host IP address. This is extremely useful for those who tend to work remotely
on several machines at the same time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/whereami
%{_mandir}/man1/whereami.1*

%changelog
%autochangelog
