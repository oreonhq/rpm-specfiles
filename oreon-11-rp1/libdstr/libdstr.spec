%global source0_hash 863bde613edada6c5330cf3a3b8f457760c209be7bf242086fd4276431515219
Name:		libdstr
Epoch:		1
Version:	1.1
Release:        1%{?dist}
Summary:        Dave's String class
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.flaterco.com/util/index.html
Source0:        https://flaterco.com/files/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%{__mv} \
	$RPM_BUILD_ROOT%{_includedir}/Dstr \
	$RPM_BUILD_ROOT%{_includedir}/Dstr.h
find $RPM_BUILD_ROOT -name '*.la' \
	-exec %{__rm} -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdstr-devel -f %{oreon_filedir}/libdstr-devel.list

%changelog

%autochangelog
