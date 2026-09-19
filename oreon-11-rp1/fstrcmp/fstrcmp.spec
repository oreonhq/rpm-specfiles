%global source0_hash e4018e850f80700acee8da296e56e15b1eef711ab15157e542e7d7e1237c3476

Name:           fstrcmp
Version:        0.7.D001
Release:        27%{?dist}
Summary:        Fuzzy string compare library

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://fstrcmp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  man-db
BuildRequires: make

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
# make t0001a ... t0010a
make $(seq -f "t%04ga" 1 10)

%install
%make_install
find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -delete

# Fix permissions
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*

# Remove useless compilation instructions
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/building.pdf
# Remove API documentation in main subpackage
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/reference.pdf
# Remove duplicate README in PDF
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/readme.pdf

%ldconfig_scriptlets

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}*.1.*

%files devel
%doc etc/reference.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.*

%changelog
%autochangelog
