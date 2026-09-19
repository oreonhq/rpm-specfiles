%global source0_hash e3f807b8cf787be384ab1dabf4ba696f656eef7014677ca1c6006f28c0cedb62

Name:           lsb_release
Version:        3.3
Release:        8%{?dist}
Summary:        Linux Standard Base Release Tool using os-release(5)

License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/lsb-release_os-release
Source:         %{url}/archive/v%{version}/lsb-release_os-release-%{version}.tar.gz

BuildRequires:  make
# For the modified vendored copy of help2man required to make the man page
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(POSIX)

# Because sometimes there's just too much minimization
Requires:       /usr/bin/getopt
Requires:       /usr/bin/sed
Requires:       /usr/bin/tr

# In case people use the debian name for this package...
Provides:       lsb-release = %{version}-%{release}

# This is intended to be an alternative to the "full" redhat-lsb version, and
# contains a conflicting /usr/bin/lsb_release file.  Originally this file was
# in redhat-lsb-core, but it was later moved to redhat-lsb.
# https://src.fedoraproject.org/rpms/redhat-lsb/c/af8e1f64209356057412fa13e686ea93180a610a
Conflicts:      redhat-lsb-core < 5.0-0.7.20231006git8d00acdc
Conflicts:      redhat-lsb >= 5.0-0.7.20231006git8d00acdc

BuildArch:      noarch

%description
Linux Standard Base Release Tool, ported to use os-release(5)
as the data source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lsb-release_os-release-%{version} -p1

%build
make

%install
make install INSTALL_ROOT=%{buildroot}%{_prefix}

%files
%license COPYING
%doc README
%{_bindir}/lsb?release
%{_mandir}/man1/lsb?release.1*

%changelog
%autochangelog
