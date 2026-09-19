%global source0_hash b313382ffea0e4a65a0d6730ce4492b1654d1bba7e11697c8552a02ad34cd4a7

Name:           libason
Version:        0.1.2
Release:        28%{?dist}
Summary:        A library for manipulating ASON values

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL: https://github.com/sadmac7000/libason
Source0: https://sadmac.fedorapeople.org/libason-0.1.2.tar.xz
Patch0: doc-fix-install-hook.patch

BuildRequires:  gcc
BuildRequires:  lemon, readline-devel
BuildRequires: make

%description
ASON is an extension of JSON which specifies a semantic, and allows for pattern
expressions that can specify or match groups of JSON values. libason is a
simple library for manipulating ASON programmatically in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

for i  in `find $RPM_BUILD_ROOT/%{_mandir} -type l`; do
	ln -f -r -s `readlink $i` $i
done

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.*
%{_bindir}/asonq
%{_mandir}/man1/*

%files devel
%doc COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
%autochangelog
