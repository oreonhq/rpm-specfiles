%global source0_hash 888a31631a7a70308bb2f333e077d0416f4bb78317f8697ffb4a95187f677301
Name:           html-xml-utils
Version:        8.8
Release:        1%{?dist}
Summary:        A number of simple utilities for manipulating HTML and XML files
License:        W3C AND BSD-3-Clause
URL:            https://www.w3.org/Tools/HTML-XML-utils/
Source0:        https://www.w3.org/Tools/HTML-XML-utils//%{name}-%{version}.tar.gz
Patch:          %{name}-c23.patch
Patch:          %{name}-libcurl.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  libcurl-devel
BuildRequires:  libidn2-devel
BuildRequires:  make
# /oreon:deps
%description
A number of simple utilities for manipulating HTML and XML files. See Manpages
for each specific command.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Force generated files to be regenerated
rm dtd.c html.c scan.c unent.c

%build

export CFLAGS='%{build_cflags} -DYY_NO_INPUT'
%configure
make
%install
%make_install
rm %{buildroot}%{_docdir}/html-xml-utils/COPYING
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
