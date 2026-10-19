%global source0_hash ac0bfb4f6c0f89a21a9436bac93f2d73696ca29121ec0772c307cabd78e47296
%global forgeurl https://github.com/wuyongzheng/gimgtools
%global date 20130918
%global commit 92d015749e105c5fb8eb704ae503a5c7e51af2bd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           gimgtools
Version:        0.03^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Garmin Image Tools
License:        GPL-2.0-only
URL:            https://code.google.com/archive/p/gimgtools/
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{forgeurl}/pull/3.patch
Patch:          %{forgeurl}/pull/7.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
gimgtools is a set of command-line tools to examine and manipulate Garmin IMG
(the map format) files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%make_build \
  CC="$CC" \
  CFLAGS="-Wall -D_FILE_OFFSET_BITS=64 $CFLAGS" \
  LDLIBS="$LDFLAGS -lm"
%install
for bin in cmdc gimgch gimgextract gimginfo gimgfixcmd gimgunlock gimgxor; do
  install -Dpm0755 -t %{buildroot}%{_bindir} "$bin"
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
