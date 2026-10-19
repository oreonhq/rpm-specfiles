%global source0_hash d8fad69a754f14e73e89715bbdbe26be54935f6c5922d5bc04dbb35f1edae42d
%global commit 7c0562c49e8f33d089f78a76a0f46d8f8a04a9b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20201019
Name:           tiosmod
Version:        0.2.7^%{date}g%{shortcommit}
Release:        1%{?dist}
Summary:        Generic patcher for Texas Instruments calculators
License:        GPL-2.0-only AND WTFPL
URL:            https://github.com/debrouxl/tiosmod
Source0:        https://github.com/debrouxl/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Suggests:       rabbitsign
# oreon:deps
BuildRequires:  gcc
# /oreon:deps
%description
tiosmod is a computer-based unlocking and optimizing program aimed at official
TI-68k calculators OS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

$CC $CFLAGS -c -o amspatch.o amspatch.c
$CC $CFLAGS -o tiosmod amspatch.o $LDFLAGS
%install
install -Dpm0755 -t %{buildroot}%{_bindir} tiosmod
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
