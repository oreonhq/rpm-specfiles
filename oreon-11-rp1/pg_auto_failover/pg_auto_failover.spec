%global source0_hash 13bcfb08fe3381e9b9e68f04affc6b0a13ae53463dfaea113824e0e7fab9354b
%bcond_without docs
%bcond_with llvmjit
%global precise_version %{?epoch:%epoch:}%version-%release
Name:           pg_auto_failover
Version:        2.1
Release:        6%{?dist}
Summary:        Postgres extension and service for automated failover and high-availability
License:        Apache-1.0
URL:            https://github.com/hapostgres/%{name}/
Source0:        https://github.com/hapostgres/%{name}/archive/refs/tags/v%{version}.tar.gz
%if %{with docs}
%endif
Recommends:     openssl
Requires:       postgresql-server postgresql-contrib
%if %{with docs}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  latexmk
BuildRequires:  libxslt-devel
BuildRequires:  lz4-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  poppler-utils
BuildRequires:  postgresql-server-devel
BuildRequires:  postgresql-static
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  readline-devel
BuildRequires:  tex(luatex85.sty)
BuildRequires:  tex(standalone.cls)
BuildRequires:  texlive-scheme-basic
BuildRequires:  zlib-devel
# /oreon:deps
%package docs
Summary:        Extra documentation for pg_auto_failover
License:        ASL 1.0 and MIT and BSD
Requires:       %{name} = %precise_version
BuildArch:      noarch
%endif
%if %{with llvmjit}
%package llvmjit
Summary:        Just-in-time compilation support for pg_auto_failover
License:        ASL 1.0
Requires:       %{name}%{?_isa} = %precise_version
Requires:       postgresql-llvmjit
%endif
%description
pg_auto_failover is an extension and service for PostgreSQL that monitors and
manages automated failover for a Postgres cluster. It is optimized for
simplicity and correctness and supports Postgres 10 and newer.
We set up one PostgreSQL server as a monitor node as well as a primary and
secondary node for storing data. The monitor node tracks the health of the
data nodes and implements a failover state machine. On the PostgreSQL nodes,
the pg_autoctl program runs alongside PostgreSQL and runs the necessary
commands to configure synchronous streaming replication.

%if %{with docs}
%description docs
The pg_auto_failover-docs package contains some additional documentation for
pg_auto_failover. Currently, this includes the main documentation in HTML
format.
%endif

%if %{with llvmjit}
%description llvmjit
This packages provides JIT support for pg_auto_failover.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p2

%build

%{_bindir}/make -O -j8 V=1 VERBOSE=1
%{_bindir}/make man
%if %{with docs}
    %{_bindir}/make -C docs html
%endif
%install
%make_install
for f in docs/_build/man/*\ *; do
    %{__mv} "$f" "${f// /_}";
done
%if %{with llvmjit}
%{__rm} -r %{buildroot}/%{_libdir}/pgsql/bitcode
%endif
%{_bindir}/install -p -D -m 0644 docs/_build/man/*.1 -t %{buildroot}%{_mandir}/man1
%{_bindir}/install -p -D -m 0644 docs/_build/man/*.5 -t %{buildroot}%{_mandir}/man5
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pg_auto_failover-docs -f %{oreon_filedir}/pg_auto_failover-docs.list

%changelog

%autochangelog
