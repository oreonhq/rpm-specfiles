%global source0_hash b1ab3db52dca36af3699178b8d0e936a30107f8d5c86a974163c580823b01790
Name:           task-spooler
Version:        1.0.4
Release:        1%{?dist}
Summary:        Personal job scheduler
License:        GPL-2.0-only AND LicenseRef-LDP-1
URL:            http://vicerveza.homeunix.net/~viric/soft/ts
Source0:        http://vicerveza.homeunix.net/~viric/soft/ts/ts-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Task spooler is a Unix batch system where the tasks spooled run one
after the other. Each user in each system has his own job queue. The tasks are
run in the correct context (that of enqueue) from any shell/process, and its
output/results can be easily watched. It is very useful when you know that
your commands depend on a lot of RAM, a lot of disk use, give a lot of
output, or for whatever reason it's better not to run them at the same time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ts-%{version}
%oreon_prep
%build

export CFLAGS="${CFLAGS} -ansi"
%make_build
%install
%make_install PREFIX=%{buildroot}%{_prefix}
mv %{buildroot}%{_bindir}/ts %{buildroot}%{_bindir}/tsp
mv %{buildroot}%{_mandir}/man1/ts.1 %{buildroot}%{_mandir}/man1/tsp.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
