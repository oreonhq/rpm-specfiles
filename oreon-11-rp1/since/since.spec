%global source0_hash 739b7f161f8a045c1dff184e0fc319417c5e2deb3c7339d323d4065f7a3d0f45
Name:		since
Version:	1.1
Release:        33%{?dist}
Summary:        Stateful tail replacement
License:	GPL-3.0-or-later
URL:		http://welz.org.za/projects/%{name}
Source0:        http://welz.org.za/projects/%{name}/%{name}-%{version}.tar.gz
%if 0%{?el5}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Since is a Unix utility similar to tail. Unlike tail, since only shows
the lines appended since the last time. It is useful to monitor
growing log files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make CFLAGS='%{optflags} -DVERSION=\"%{version}\"' %{?_smp_mflags}
%install
%if 0%{?el5}
rm -rf $RPM_BUILD_ROOT
%endif
make install prefix=$RPM_BUILD_ROOT/%{_prefix} INSTALL='install -Dp'
chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
