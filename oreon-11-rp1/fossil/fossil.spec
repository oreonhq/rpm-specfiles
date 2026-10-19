%global source0_hash 84c18824ca227e7602d2408b663c3747f754ad306ed5c73ddab959d6589538a6
%bcond_without tests
Name:             fossil
Version:          2.28
Release:        1%{?dist}
Summary:        A distributed SCM with bug tracking and wiki
License:          LicenseRef-Callaway-BSD
URL:              https://www.fossil-scm.org/
Source0:        https://www.%{name}-scm.org/home/tarball/version-%{version}/%{name}-src-%{version}.tar.gz
Source1:          template.config
Source2:          fossil-doc
Source3:          fossil-doc-README
Provides:         bundled(sqlite) = 3.38.0
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sqlite
BuildRequires:  tcl
BuildRequires:  zlib-devel
# /oreon:deps
%description
Fossil is a simple, high-reliability, distributed software configuration
management with distributed bug tracking, distributed wiki and built-in web
interface.

%package doc
Summary:          Fossil documentation
Requires:         fossil
%description doc
Documentation in repository format for %{name}. Users can run `fossil ui`
in %{_docdir}/%{name}-doc folder to view documents in browser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n fossil-src-%{version}

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
for conf in /usr/lib/rpm/config.*; do [ -z "${f}" ] && break; cp "${f}" autosetup; done

%build

%set_build_flags
./configure --build=%{_build} \
  --disable-dependency-tracking \
  --prefix=%{_prefix} \
  --exec-prefix=%{_exec_prefix} \
  --bindir=%{_bindir} \
  --sbindir=%{_sbindir} \
  --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --localstatedir=%{_localstatedir} \
  --sharedstatedir=%{_sharedstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --with-openssl=auto \
  --json
%make_build
chmod -x www/collisions.ipynb
sed -i "s:^#\!/usr/bin/env\s\+tclsh\s\?$:#!%_bindir/tclsh:" www/mkindex.tcl
%install
%make_install
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 fossil.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
tclsh test/tester.tcl %{buildroot}%{_bindir}/%name
%endif
%{buildroot}%{_bindir}/%name init --admin-user %name %name-doc.fossil
%{buildroot}%{_bindir}/%name open --force %name-doc.fossil
%{buildroot}%{_bindir}/%name configuration import %{SOURCE1}
sqlite3 %name-doc.fossil "REPLACE INTO config(name,value,mtime) VALUES('doc-glob','*.wiki,*.html,*.md,*.txt',1608172730);"
%{buildroot}%{_bindir}/%name add www
%{buildroot}%{_bindir}/%name commit --user %name --force --comment '%name-doc initial commit'
%{buildroot}%{_bindir}/%name fts-config enable d
%{buildroot}%{_bindir}/%name fts-config index on
install -m 0755 -p -D %{SOURCE2} %{buildroot}%{_bindir}
cp %{SOURCE3} README
%files -f %{oreon_filedir}/main.list
%files -n fossil-doc -f %{oreon_filedir}/fossil-doc.list

%changelog

%autochangelog
