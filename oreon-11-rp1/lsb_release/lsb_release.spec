%global source0_hash e3f807b8cf787be384ab1dabf4ba696f656eef7014677ca1c6006f28c0cedb62
Name:           lsb_release
Version:        3.3
Release:        1%{?dist}
Summary:        Linux Standard Base Release Tool using os-release(5)
License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/lsb-release_os-release
Source0:        https://github.com/thkukuk/lsb-release_os-release/archive/v%{version}/lsb-release_os-release-%{version}.tar.gz
Requires:       /usr/bin/getopt
Requires:       /usr/bin/sed
Requires:       /usr/bin/tr
Provides:       lsb-release = %{version}-%{release}
Conflicts:      redhat-lsb-core < 5.0-0.7.20231006git8d00acdc
Conflicts:      redhat-lsb >= 5.0-0.7.20231006git8d00acdc
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Linux Standard Base Release Tool, ported to use os-release(5)
as the data source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lsb-release_os-release-%{version}
%oreon_prep
%build

make
%install
make install INSTALL_ROOT=%{buildroot}%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
