%global source0_hash c6ffbc34a511ac00d072219bda30699e51f2f4eb483cbae9e32e981d49e8b380
Name:           reptyr
Version:        0.10.0
Release:        1%{?dist}
Summary:        Attach a running process to a new terminal
License:        MIT
URL:            http://github.com/nelhage/reptyr
Source0:        https://github.com/nelhage/reptyr/archive/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
Requires:       pkgconf-pkg-config
# oreon:deps
BuildRequires:  /usr/bin/python3
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  make
BuildRequires:  python3-pexpect
# /oreon:deps
%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal.  Started a long-running process over
ssh, but have to leave and don't want to interrupt it?  Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}
sed -i s/python2/python3/g Makefile

%build

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"
%find_lang %{name} --with-man
%oreon_autofiles main

%check

make test CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
