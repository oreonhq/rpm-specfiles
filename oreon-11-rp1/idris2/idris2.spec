%global source0_hash 7b85226098c5dee96a0a77c892932d2e9fab8e5a5c2d08a0525520e1f4405551
%if %{defined el9}
%global debug_package %{nil}
%endif
%global chez_version %(%{_bindir}/scheme --version 2>/dev/null || echo unknown)
%bcond scm_boot 1
%bcond docs 1
%bcond test 0
%ifarch ppc64le %{ix86}
%bcond racket 1
%else
%bcond racket 0
%endif
%if %{with racket}
%define _build_id_links alldebug
%endif
Name:           idris2
Version:        0.8.0
Release:        1%{?dist}
Summary:        Purely functional programming language with first class types
License:        BSD-3-Clause
URL:            https://www.idris-lang.org
Source0:        https://github.com/idris-lang/Idris2/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         idris2-api-mk.patch
ExcludeArch:    ppc64le s390x %{ix86}
%if %{without scm_boot}
%endif
%if %{with docs}
%endif
%if %{with test}
%endif
%if %{with racket}
Requires:       racket-minimal%{?_isa}
%else
Requires:       chez-scheme%{?_isa} = %{chez_version}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Recommends:     rlwrap
# oreon:deps
BuildRequires:  chez-scheme
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# /oreon:deps
%description
Idris is a programming language designed to encourage Type-Driven Development.

%if %{with docs}
%package doc
Summary:        Idris2 documentation
Requires:       fontawesome-fonts
BuildArch:      noarch
%description doc
The package contains the idris2 manual
%endif

%package libs
Summary:        idris2 runtime support library
Obsoletes:      %{name}-lib < %{version}-%{release}
%description libs
The package provide the runtime support library for idris2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Idris2-%{version}
%autopatch -p1

%build

%if %{with scm_boot}
make %{?with_racket:bootstrap-racket}%{!?with_racket:bootstrap SCHEME=scheme} PREFIX=%{_libdir}
%else
make
%endif
%if %{with docs}
make -C docs html
%endif
%install
export PATH=%{buildroot}/bin:$PATH
make install DESTDIR=%{buildroot} PREFIX=%{_libdir}
mkdir %{buildroot}%{_bindir}
%if %{without racket}
mv %{buildroot}%{_libdir}/bin/idris2_app/idris2.so %{buildroot}%{_bindir}/idris2
%else
mv %{buildroot}%{_libdir}/bin/idris2_app/idris2 %{buildroot}%{_bindir}/
%endif
rm %{buildroot}%{_libdir}/bin/idris2_app/libidris2_support.so
mv %{buildroot}%{_libdir}/%{name}-%{version}/lib/libidris2_support.so %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
LD_LIBRARY_PATH="%{buildroot}%{_libdir}:" %{buildroot}%{_bindir}/idris2 --bash-completion-script %{name} | sed "s/dirnames/default/" > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
make install-api DESTDIR=%{buildroot} PREFIX=%{_libdir} IDRIS2_PACKAGE_PATH=%{buildroot}%{_libdir}/%{name}-%{version} LD_LIBRARY_PATH="%{buildroot}%{_libdir}:"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with test}
%check

make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n idris2-doc -f %{oreon_filedir}/idris2-doc.list
%files -n idris2-libs -f %{oreon_filedir}/idris2-libs.list

%changelog

%autochangelog
