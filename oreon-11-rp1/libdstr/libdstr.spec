%global source0_hash 863bde613edada6c5330cf3a3b8f457760c209be7bf242086fd4276431515219

Name:		libdstr
Epoch:		1
Version:	1.1
Release:	1%{?dist}
Summary:	Dave's String class

BuildRequires:	gcc-c++
BuildRequires: make

# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/546
# SPDX confirmed
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.flaterco.com/util/index.html
Source0:	https://flaterco.com/files/%{name}-%{version}.tar.xz

%description
libdstr is a library containing Dstr, Dave's String class.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

# Upstream uses some odd header file name,
# changing...
%{__mv} \
	$RPM_BUILD_ROOT%{_includedir}/Dstr \
	$RPM_BUILD_ROOT%{_includedir}/Dstr.h

find $RPM_BUILD_ROOT -name '*.la' \
	-exec %{__rm} -f {} ';'

%ldconfig_scriptlets

%files
%doc	AUTHORS
%license	COPYING
%doc	ChangeLog
%doc	README

%{_libdir}/libdstr.so.2{,.*}

%files devel

%{_includedir}/Dstr.h
%{_libdir}/libdstr.so

%changelog
%autochangelog
