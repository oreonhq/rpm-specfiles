%global source0_hash 7d7fa6a9f5f53d607ab851d739ae3d3b99ca86e2cb1425a6cab9299f673aee16

%global owner neurobin

Name: shc
Summary: Shell script compiler
URL: https://neurobin.org/projects/softwares/unix/shc/
Version: 4.0.3
Release: 16%{?dist}
Source0: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
BuildRequires: make
BuildRequires: gcc

%description
SHC is a generic shell script compiler. It takes
a script, which is specified on the command line
and produces C source code. The generated source
code is then compiled and linked to produce a s-
tripped binary. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README README.md
%{_bindir}/%{name}
%{_mandir}/*/%{name}*

%changelog
%autochangelog
