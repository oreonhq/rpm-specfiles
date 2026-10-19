%global source0_hash 7bfc8d40744ed5d0f1f97008cc58f5dc05b1688c348f5f58c076c924bc323373
%global date 20121105
%global hash c55cb50
%global checkout %{date}git%{hash}
%global tarbase pmachata-dwlocstat-%{hash}
Name: dwlocstat
Version: 0.1
Release:        1%{?dist}
Summary:        Tool for examining Dwarf location info coverage
License: GPL-3.0-or-later AND LGPL-3.0-or-later
URL: https://github.com/pmachata/dwlocstat
Source0:        https://github.com/pmachata/%{name}/tarball/%{hash}/%{tarbase}.tar.gz
Patch0:  dwlocstat-remove-DW_TAG_mutable_type.patch
# oreon:deps
BuildRequires:  elfutils-devel
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
dwlocstat is a tool for examining Dwarf location info coverage.  It
goes through DIEs of given binary's debug info that represent
variables and function parameters.  For each such DIE, it computes
coverage of that DIE's range by location expressions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarbase}
%patch -P0 -p1

%build

make %{?_smp_mflags} dwlocstat \
     CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 -t $RPM_BUILD_ROOT%{_bindir} dwlocstat
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 -t $RPM_BUILD_ROOT%{_mandir}/man1 %{name}.1
%oreon_autofiles main

%check

./dwlocstat ./dwlocstat
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
