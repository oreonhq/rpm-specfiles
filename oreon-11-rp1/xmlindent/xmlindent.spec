%global source0_hash 3a0f6887b696087b8dad4901d3994954214dbbd78499eaf622b9a85060cf254c
Name: xmlindent
Version: 0.2.17
Release:        1%{?dist}
Summary:        XML stream reformatter
License: GPL-2.0-or-later
URL: http://xmlindent.sf.net/
Source0:        http://downloads.sourceforge.net/xmlindent/xmlindent-%{version}.tar.gz
# oreon:deps
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
XML Indent is a XML stream reformatter written in ANSI C.
It is analogous to GNU indent.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i -e "s,-Wall,-Wall \$(CFLAGS),g" -e "s,555,755," -e "s,444,644," Makefile

%build

CFLAGS=$RPM_OPT_FLAGS make %{?_smp_mflags}
%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
