%global source0_hash 92835552b1b687ad26737e429b5aba36510bf429f8816ec0f6d336c8cb41f443
%global bootstrap 1
%global shortversion 6.0.0
%global libver 11
Name:           chicken
Version:        %{shortversion}
Release:        1%{?dist}
Summary:        A practical and portable Scheme system
License:        BSD-3-Clause
URL:            http://call-cc.org
Source0:        http://code.call-cc.org/releases/%{version}/%{name}-%{version}.tar.gz
Patch0:         make_cflags_work.patch
Requires:       chicken-libs%{?_isa} = %{version}-%{release}
Obsoletes:      chicken-doc < 4.8.0.5-3
Provides:       chicken-doc = %{version}-%{release}
%if %{bootstrap} == 0
%endif
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  make
# /oreon:deps
%package libs
Summary:        Chicken Scheme runtime library
%description libs
The Chicken Scheme runtime library, linked to by programs compiled with
Chicken.

%package static
Summary:	Static library for Chicken
Requires:	chicken%{?_isa} = %{version}-%{release}
%description static
The Chicken Scheme runtime library, as a static library for users
to link against

%description
CHICKEN is a compiler for the Scheme programming language.
CHICKEN produces portable, efficient C, supports almost all of the R5RS
Scheme language standard, and includes many enhancements and extensions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%if %{bootstrap} == 0
make PLATFORM=linux spotless
echo "#define C_BUILD_TAG \"compiled $(date '+%Y-%m-%d') on $(hostname)\"" > buildtag.h
%endif
make CFLAGS="$(echo "%{optflags}" | sed 's/-Wall//') -Wformat" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir} \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     PLATFORM=linux
%install
make CFLAGS="$(echo "%{optflags}" | sed 's/-Wall//') -Wformat" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir} \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     DESTDIR=%{buildroot} \
     PLATFORM=linux install
rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE %{buildroot}/%{_docdir}/%{name}/README
find %{buildroot} -name \*.so -exec chrpath --delete \{\} \;
chrpath --delete %{buildroot}/%{_bindir}/chicken*
chrpath --delete %{buildroot}/%{_bindir}/csc
chrpath --delete %{buildroot}/%{_bindir}/csi
%oreon_autofiles chicken-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles chicken-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make PLATFORM=linux check
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n chicken-libs -f %{oreon_filedir}/chicken-libs.list
%files -n chicken-static -f %{oreon_filedir}/chicken-static.list

%changelog

%autochangelog
