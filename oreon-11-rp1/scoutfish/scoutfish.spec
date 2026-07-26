%global source0_hash 1148760944c24a13fb26eed40243c2ed1a5a43578ee0637b0a12dd1172995340

%bcond_without tests

%global forgeurl https://github.com/pychess/scoutfish
%global commit b619262405d19ae8831fd91b2b29bd85c5b23d84
%forgemeta

Name:           scoutfish
Version:        1.1
Release:        12%{?dist}
Summary:        Chess Query Engine 

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
# PR#7 Added handling of Chess 960 PGNs, fixed offsets for extra newlines
Patch0:         %{url}/pull/7.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  sed
%if %{with tests}
BuildRequires:  python3dist(pexpect)
%endif

%description
Scoutfish lets you run powerful and flexible queries on very big chess
databases and with very high speed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1
# Fix python shebang
sed -e 's:/usr/bin/env python:/usr/bin/python3:' -i src/*.py
# Drop arch bitness flags as they break the build on ARM
sed -e 's:-m$(bits)::g' -i src/Makefile

%build
pushd src
%make_build build \
  ARCH="general-%{__isa_bits}" \
  EXTRACXXFLAGS="%{optflags}" \
  EXTRALDFLAGS="${build_ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 src/scoutfish %{buildroot}%{_bindir}/

%if %{with tests}
%check
pushd src
%python3 test.py
%endif

%files
%license Copying.txt
%doc README.md src/scoutfish.py
%{_bindir}/scoutfish

%changelog
%autochangelog
