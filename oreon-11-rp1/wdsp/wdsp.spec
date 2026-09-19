%global source0_hash 30491b3f85d57ac40889cd3494649b8fa46304f6d6ef40de8585a8eb5bcd3de9

# git ls-remote git://github.com/jimahlstrom/wdsp
%global git_commit 18782be8d7e75bf7e41e1f23e912640de8d6ce58
%global git_date 20250922

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		wdsp
Version:	0
Release:	0.13.%{git_suffix}%{?dist}
Summary:	DSP library for LinHPSDR
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/jimahlstrom/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	fftw-devel
BuildRequires:	pkgconfig(gtk+-3.0)
Patch0:		wdsp-0-soname-add.patch

%description
DSP library for LinHPSDR.

%package devel
Summary:	Development files for wdsp
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for wdsp.

%package doc
Summary:	Documentation files for wdsp
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation files for wdsp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{git_commit} -p1

%build
cd build_shared
%make_build CFLAGS="%{build_cflags} -fPIC -D _GNU_SOURCE" LDFLAGS="%{build_ldflags}"

%install
install -Dpm 0775 -t %{buildroot}%{_libdir} ./libwdsp.so.0.*
cp ./libwdsp.so "%{buildroot}%{_libdir}/libwdsp.so"
install -Dpm 0664 src/wdsp.h "%{buildroot}%{_includedir}/wdsp.h"
install -Dpm 0664 "WDSP Guide, Rev 1.25.pdf" %{buildroot}/%{_docdir}/%{name}/"WDSP Guide, Rev 1.25.pdf"

%files
%doc README.md
%license GNU_GENERAL_PUBLIC_LICENSE.txt
%{_libdir}/libwdsp.so.0*

%files devel
%{_includedir}/wdsp.h
%{_libdir}/libwdsp.so

%files doc
%{_docdir}/%{name}/WDSP\ Guide\,\ Rev\ 1.25.pdf

%changelog
%autochangelog
