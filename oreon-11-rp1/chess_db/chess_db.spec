%global source0_hash 0f61d4eb4535bb3392c23063c80554b50db661337d9a1cd65b5cbdbea2edd729

%bcond_without tests

%global forgeurl https://github.com/pychess/chess_db
%global commit eb41ddf4cb5eb6ef5eedaa4d9006f4d2e8a60dd6
%forgemeta

Name:           chess_db
Version:        0.2
Release:        14%{?dist}
Summary:        Chess database opening tree indexer

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  sed
%if %{with tests}
BuildRequires:  python3dist(pexpect)
%endif

%description
This project helps index PGN files to polyglot books with the standard moves
and weights, but also has Win/Loss/Draw Stats and game_index information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
# Fix python shebang
sed -e 's:/usr/bin/env python:/usr/bin/python3:' -i parser/*.py
# Drop arch bitness flags as they break the build on ARM
sed -e 's:-m$(bits)::g' -i parser/Makefile

%build
pushd parser
%make_build build \
  ARCH="general-%{__isa_bits}" \
  EXTRACXXFLAGS="%{optflags}" \
  EXTRALDFLAGS="${build_ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 parser/parser %{buildroot}%{_bindir}/

%if %{with tests}
%check
pushd parser
%python3 test.py
%endif

%files
%license Copying.txt
%doc README.md parser/chess_db.py
%{_bindir}/parser

%changelog
%autochangelog
