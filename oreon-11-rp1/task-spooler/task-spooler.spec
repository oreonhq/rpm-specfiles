%global source0_hash fa833311543dc535b60cb7ab83c64ab5ee31128dbaaaa13dde341984e542b428

Name:           task-spooler
Version:        1.0.3
Release:        1%{?dist}
Summary:        Personal job scheduler

# Licence headers in code files say:
# > Please find the license in the provided COPYING file.
# COPYING contains the GPL-2.0 text.
# There's no mention of "or later version" anywhere.
#
# tsp.1 is subject to "LDP GENERAL PUBLIC LICENSE".
License:        GPL-2.0-only AND LicenseRef-LDP-1

URL:            http://vicerveza.homeunix.net/~viric/soft/ts
Source0:        %{url}/ts-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
Task spooler is a Unix batch system where the tasks spooled run one
after the other. Each user in each system has his own job queue. The tasks are
run in the correct context (that of enqueue) from any shell/process, and its
output/results can be easily watched. It is very useful when you know that
your commands depend on a lot of RAM, a lot of disk use, give a lot of
output, or for whatever reason it's better not to run them at the same time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ts-%{version}

%build
export CFLAGS="${CFLAGS} -ansi"
%make_build

%install
%make_install PREFIX=%{buildroot}%{_prefix}
mv %{buildroot}%{_bindir}/ts %{buildroot}%{_bindir}/tsp
mv %{buildroot}%{_mandir}/man1/ts.1 %{buildroot}%{_mandir}/man1/tsp.1

%files
%license COPYING
%doc Changelog README TRICKS PROTOCOL
%{_bindir}/tsp
%{_mandir}/man1/tsp.1.*

%changelog
%autochangelog
