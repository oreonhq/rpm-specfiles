%global source0_hash 599a30b61dfafe563ec4f16bdfaed884d77cf95f989a57160193b77a437115c3
%global git_commit 7e94881a6059a824efaed41301c4a89a384d86a2
%global git_date 20180117
%global git_short_commit %(c=%{git_commit}; echo ${c:0:8})
%global git_suffix %{git_date}git%{git_short_commit}
Name:		hidrd
Version:	0.2.0
Release:        1%{?dist}
Summary:        HID report descriptor I/O library and conversion tool
License:	GPL-2.0-or-later
URL:		https://github.com/DIGImend/hidrd
Source0:        https://github.com/DIGImend/%{name}/archive/%{git_commit}.tar.gz#/%{name}-%{version}-%{git_date}git%{git_short_commit}.tar.gz
Patch:		hidrd-2.0.0-nonstring-workaround.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%package devel
Summary:	Development files needed for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%description
Hidrd is a library and a tool for reading, writing and converting HID report
descriptors in/between various formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{git_commit} -p1
./bootstrap

%build

%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%check

make check
%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hidrd-devel -f %{oreon_filedir}/hidrd-devel.list

%changelog

%autochangelog
