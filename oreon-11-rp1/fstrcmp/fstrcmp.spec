%global source0_hash e4018e850f80700acee8da296e56e15b1eef711ab15157e542e7d7e1237c3476
Name:           fstrcmp
Version:        0.7.D001
Release:        1%{?dist}
Summary:        Fuzzy string compare library
License:        GPL-3.0-or-later
URL:            http://fstrcmp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  man-db
# /oreon:deps
%description
The fstrcmp package provides a library which may be used to make fuzzy
comparisons of strings and byte arrays. It also provides simple commands for use
in shell scripts.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%check

make $(seq -f "t%04ga" 1 10)
%install
%make_install
find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -delete
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/building.pdf
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/reference.pdf
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/readme.pdf
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fstrcmp-devel -f %{oreon_filedir}/fstrcmp-devel.list

%changelog

%autochangelog
