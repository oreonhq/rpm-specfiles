%global source0_hash b8127fb6fe5562dfabfcb7d62df4ba2f018de39d7fbe7df2b7a688578516b4b7
%global docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
Name:		QuantLib
Version:	1.29
Release:        9%{?dist}
Summary:        A software framework for quantitative finance
License:	LicenseRef-Callaway-BSD
URL:		http://www.quantlib.org
Source0:        https://dl.bintray.com/quantlib/releases/QuantLib-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
# /oreon:deps
%description
QuantLib is a free/open-source library for modeling, trading, and 
risk management in real-life.

%package devel
Summary:	QuantLib development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Static libraries and headers for QuantLib.

%package test
Summary:	The test-suite to check the setup of QuantLib
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description test
The QuantLib-test-suite will validate the compiled code against 
pre-constructed test cases, and helps in validating the library.

%package doc
Summary:	The documentation for QuantLib
Requires:	%{name} = %{version}
BuildRequires:	doxygen >= 1.3, graphviz
%description doc
This package contains documentation files generated from the source code of
QuantLib.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --enable-intraday CFLAGS="$RPM_OPT_FLAGS -fpermissive" CPPFLAGS="$RPM_OPT_FLAGS -fpermissive"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{docdir}
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p man/*.1 %{buildroot}%{_mandir}/man1/
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/*.a
touch -r News.md %{buildroot}%{_bindir}/quantlib-config
touch -r News.md %{buildroot}%{_datadir}/emacs/site-lisp/quantlib.elc
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
