%global source0_hash daa53c0dc2d18d7265a862bee8a5b502d6c8f692f00674a635f3117b3926d594
Name:		f3
Version:	10.0
Release:        1%{?dist}
Summary:        Utility to test for fake flash drives and cards
License:	GPL-3.0-only
URL:		https://oss.digirati.com.br/f3/
Source0:        https://github.com/AltraMayor/%{name}/archive/v%{version}/%{name}-%{version}.zip
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  parted-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
F3 is a utility to test for fake flash drives and cards. It is a Free
Software alternative to h2testw.  f3write will fill the unused part of
a filesystem with files NNNN.fff with known content, and f3read will
analyze the files to determine whether the contents are corrupted, as
happens with fake flash.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e 's/gcc/gcc $(CFLAGS)/' Makefile

%build

%make_build CFLAGS="%{optflags}" all extra
%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 f3read f3write f3probe f3brew f3fix %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 f3read.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
