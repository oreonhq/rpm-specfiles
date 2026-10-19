%global source0_hash f2085819d03f4e407a8dfcf36bdafcc83259bbad3b483a255f5d4ca45087161b
Summary:        Hessu's Tampa Ping-Pong conversd URO modified version
Name: htppu
Version: 1.8
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://sourceforge.net/projects/htppu/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: htppu-1.8-install-fix.patch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The URO modified Ping-Pong conversd, derived from WAMPES' conversd
by Dieter Deyke <deyke@mdddhd.fc.hp.com>. It is also used in
the Internet for ham radio conversation groups.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# remove execute permissions from everything
find . -type f -exec chmod a-x {} \;

%autopatch -p1

%build

%make_build COPTS="-DWANT_LOG %{optflags}" LDFLAGS="%{?__global_ldflags}"
%install
make install-all BASE_DIR="%{buildroot}" MAN_DIR="%{buildroot}%{_mandir}" LOG_DIR="%{buildroot}/var/log" \
  SBIN_DIR="%{buildroot}%{_sbindir}" OWN="root"
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a doc/* %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
