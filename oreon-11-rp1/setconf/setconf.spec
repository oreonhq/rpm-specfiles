%global source0_hash 0fac23fc484a2531e5a1fe0d30461eeb98d007f9b3aa4c1176fe70a5abe79986
Name:           setconf
Version:        0.7.7 
Release:        1%{?dist}
Summary:        Utility for changing settings in configuration text files
License:        GPL-2.0-only
URL:            http://setconf.roboticoverlords.org/ 
Source0:        https://github.com/xyproto/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         setconf-0.7.6-rm_sb.patch
Patch2:         setconf-0.7.7-add_man.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Setconf is small utility that can be used for
changing settings in configuration text files. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%py3_build
%check

%{__python3} setconf.py --test
awk '/^..\/setconf.py/ { print "%{__python3} " $0; next } { print }' testcases/test.sh >testcases/py3_test.sh
chmod a+x testcases/py3_test.sh
cd testcases/ && ./py3_test.sh
%install
%py3_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
