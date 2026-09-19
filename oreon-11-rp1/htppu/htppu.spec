%global source0_hash d2fa034c551f195f59c62a365e6a3f83a44be3404064325ab1f563a317206d82

Summary: Hessu's Tampa Ping-Pong conversd URO modified version
Name: htppu
Version: 1.8
Release: 13%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://sourceforge.net/projects/htppu/
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
Patch0: htppu-1.8-install-fix.patch

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

# docs
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a doc/* %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%doc %{_docdir}/%{name}
%dir %{_sysconfdir}/htppu
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/htppu/*
%{_mandir}/*/*
%{_var}/lib/htppu

%changelog
%autochangelog
