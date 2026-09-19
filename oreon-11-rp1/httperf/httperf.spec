%global source0_hash 307bef6ed06d90741aad7978d6a64610c28373151a3e13ae500bac2d17d9d388

%global forgeurl https://github.com/httperf/httperf/
%global commit 6342b166b1eaffd178d08da31e506540d91f2e17
%forgemeta

Name:           httperf
Version:        0.9.1
Release:        0.16%{?dist}
Summary:        Tool for measuring web server performance
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         httperf-signal.patch
Patch1:         httperf-autoconf.patch
Patch2:         httperf-compiler-warning.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  autoconf automake libtool

%description
Httperf is a tool for measuring web server performance. It provides a
flexible facility for generating various HTTP workloads and for
measuring server performance. The focus of httperf is not on
implementing one particular benchmark but on providing a robust,
high-performance tool that facilitates the construction of both micro-
and macro-level benchmarks. The three distinguishing characteristics
of httperf are its robustness, which includes the ability to generate
and sustain server overload, support for the HTTP/1.1 and SSL
protocols, and its extensibility to new workload generators and
performance measurements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
autoreconf -vif
%configure --enable-idleconn
%make_build

%install
%make_install

# fix permissions
chmod -x AUTHORS ChangeLog NEWS README.md TODO COPYRIGHT

%files
%{_bindir}/httperf
%{_bindir}/idleconn
%{_mandir}/man1/httperf.1*
%{_mandir}/man1/idleconn.1*
%license COPYRIGHT
%doc AUTHORS ChangeLog NEWS README.md TODO

%changelog
%autochangelog
