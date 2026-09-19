%global source0_hash 599a30b61dfafe563ec4f16bdfaed884d77cf95f989a57160193b77a437115c3

%global git_commit 7e94881a6059a824efaed41301c4a89a384d86a2
%global git_date 20180117

%global git_short_commit %(c=%{git_commit}; echo ${c:0:8})
%global git_suffix %{git_date}git%{git_short_commit}

Name:		hidrd
Version:	0.2.0
Release:	27.%{git_suffix}%{?dist}
Summary:	HID report descriptor I/O library and conversion tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/DIGImend/hidrd
Source0:	https://github.com/DIGImend/hidrd/archive/%{git_commit}.tar.gz#/%{name}-%{version}-%{git_suffix}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libxml2-devel
# Upstream PR: https://github.com/DIGImend/hidrd/pull/33
Patch:		hidrd-2.0.0-nonstring-workaround.patch

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
# fix unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%check
make check

%install
%make_install
# remove .a/.la files
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/hidrd-convert
%{_libdir}/lib%{name}*.so.*
%{_datadir}/xml

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}

%changelog
%autochangelog
