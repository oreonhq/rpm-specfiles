%global source0_hash de16ff10452869cbdc056aedbfeadc612a612e97d35a1c75d0cef7bcd7ed9673
Name:       smatch
Version:    1.75
Release:        1%{?dist}
Summary:        A static analyzer for C
License:    GPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:        https://%{name}.sourceforge.net
Source0:        https://github.com/error27/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:     do-not-build-sparse-binaries.patch
Patch1:     fix-datadir-path.patch
Patch2:     use-distribution-ldflags.patch
Patch3:     preserve-install-timestamps.patch
Patch4:     add-BSD-3-license.patch
Requires: %{name}-data = %{version}-%{release}
Provides: bundled(cwchash)
Provides: bundled(sparse)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Smatch is a static analysis tool for C.

%package data
Summary: Data for Smatch the C static analyzer
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description data
Data for Smatch the static analysis tool for C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PREFIX='%{_prefix}'
%install
%make_install PREFIX='%{_prefix}'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

echo 'int main(void) { int a[2]; return a[2]; }' > test.c
./smatch test.c 2>&1 | tee out
grep "test.c:1 main() error: buffer overflow 'a' 2 <= 2" out
%files -f %{oreon_filedir}/main.list
%files -n smatch-data -f %{oreon_filedir}/smatch-data.list

%changelog

%autochangelog
