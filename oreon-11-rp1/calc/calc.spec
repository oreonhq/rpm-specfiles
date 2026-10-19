%global source0_hash cb5b0576c3d206ed55b6929cc3a1ebc5afedbfdc70d528274cbac8e650c56d77
%define with_readline 1
%define with_custom_interface 1
License:       LGPL-2.1-only AND Unlicense
Name:          calc
Version:       3.0.1.0
Release:        1%{?dist}
Summary:        Arbitrary precision arithmetic system and calculator
URL:           http://isthe.com/chongo/tech/comp/calc/
Source0:        https://github.com/lcn2/calc/releases/download/v%{version}/calc-%{version}.tar.gz
Provides:      apcalc
%if %{with_readline}
%endif
Recommends:    less >= 358
Recommends:    %{name}-stdrc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  sed
BuildRequires:  util-linux
# /oreon:deps
%description
Calc is an arbitrary precision C-like arithmetic system that is a
calculator, an algorithm-prototyper, and a mathematical research tool. Calc
comes with a rich set of built-in mathematical and programmatic functions.

%package libs
Summary:       Libraries for the calc arithmetic system
%description libs
Shared libraries used by the calc command line calculator and other programs
using its arbitrary precision arithmetic routines.

%package devel
Summary:        Development files for the calc arithmetic system
Requires:       %{name}-libs = %{version}-%{release}
%description devel
This package contains files necessary to build applications which use the
calc arbitrary precision arithmetic system.

%package stdrc
Summary:      Standard resource files the calc arithmetic system
Requires:     %{name} = %{version}-%{release}
%description stdrc
This package contains the standard calc resource files and several calc
shell scripts. They serve as examples of the calc language and may also be
useful in themselves.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make DEBUG="%{optflags}" \
%if %{with_custom_interface}
     ALLOW_CUSTOM="-DCUSTOM" \
%else
     ALLOW_CUSTOM="-UCUSTOM" \
%endif
     LD_SHARE="" \
%if %{with_readline}
     USE_READLINE="-DUSE_READLINE" \
     READLINE_LIB="-lreadline" \
     READLINE_EXTRAS="" \
%else
     USE_READLINE="" \
%endif
     HAVE_FPOS="-DHAVE_NO_FPOS" \
     ARCH_CFLAGS="" \
     PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     Q="" V="@" \
     all
%install
make T=%{buildroot} \
%if %{with_custom_interface}
     ALLOW_CUSTOM="-DCUSTOM" \
%else
     ALLOW_CUSTOM="-UCUSTOM" \
%endif
     PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     SCRIPTDIR=%{_datadir}/%{name}/cscript \
     install
%if %{with_readline} 
  rm -f %{buildroot}/%{_datadir}/%{name}/bindings
%endif
%if ! %{with_custom_interface}
  rm %{buildroot}/%{_libdir}/libcustcalc.so*
  chmod +w %{buildroot}/%{_datadir}/calc/custhelp/*
  chmod +w %{buildroot}/%{_datadir}/calc/custom/*
  rm %{buildroot}/%{_datadir}/calc/custhelp/*
  rm %{buildroot}/%{_datadir}/calc/custom/*
  rmdir %{buildroot}/%{_datadir}/calc/custhelp
  rmdir %{buildroot}/%{_datadir}/calc/custom/
%endif
chmod 755 %{buildroot}%{_datadir}/%{name}/cscript/*
chmod 755 %{buildroot}%{_bindir}/calc
chmod 755 %{buildroot}/%{_libdir}/libcalc.so.%{version}
mv %{buildroot}%{_datadir}/%{name}/README README-standard-resource
mv cscript/README README-cscript
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make chk
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n calc-libs -f %{oreon_filedir}/calc-libs.list
%files -n calc-devel -f %{oreon_filedir}/calc-devel.list
%files -n calc-stdrc -f %{oreon_filedir}/calc-stdrc.list

%changelog

%autochangelog
