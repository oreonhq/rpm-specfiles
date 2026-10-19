%global source0_hash f5db8c1fed5276aa90e58eea53c3cbe5e81f123057240191a8fc86a8404627d3
Name:           sblg
Version:        0.6.1
Release:        1%{?dist}
Summary:        Static blog utility
%global ver     %(v=%{version}; echo ${v//\./_})
License:        ISC
URL:            https://kristaps.bsd.lv/sblg/
VCS:            git:https://github.com/kristapsdz/sblg.git
Source0:        https://github.com/kristapsdz/%{name}/archive/VERSION_%{ver}/%{name}-VERSION_%{ver}.tar.gz
Recommends:  lowdown
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  valgrind
# /oreon:deps
%description
sblg is a utility for creating static blogs. It merges articles into templates
to generate static HTML files, Atom feeds, and JSON files. It's built for use
with make. No PHP, no database, just a simple UNIX tool for pulling data from
articles and populating templates. 

%package doc
BuildArch: noarch
Summary: Static blog utility
%description doc
Examples and documentation for sblg.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sblg-VERSION_%{ver}

%build

./configure PREFIX=%{_prefix} MANDIR=%{_mandir} SHAREDIR=%{_docdir} LDFLAGS="${LDFLAGS}"
%make_build
%install
%make_install
chmod 755 %{buildroot}/%{_bindir}/sblg
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make regress
make valgrind
%files -f %{oreon_filedir}/main.list
%files -n sblg-doc -f %{oreon_filedir}/sblg-doc.list

%changelog

%autochangelog
