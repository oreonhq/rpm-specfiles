%global source0_hash d14b1568b6db8cd51659e3cc476a1f45da2020434ebb90b4b0defbc424f05907

%{!?tcl_version: %global tcl_version %((echo '8.6'; echo 'puts $tcl_version' | tclsh 2> /dev/null) | tail -n 1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

%global pkgname tclreadline

Summary:        GNU Readline extension for Tcl/Tk
Name:           tcl-tclreadline
Version:        2.4.1
Release:        3%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/flightaware/tclreadline
Source0:        https://github.com/flightaware/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
Patch0:         tcl-tclreadline-2.4.0-libdir.patch
Patch1:         https://github.com/flightaware/tclreadline/pull/62.patch#/tcl-tclreadline-2.4.1-version.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
BuildRequires:  readline-devel
BuildRequires:  autoconf%{?el8:2.7x}%{?el9:2.7x}
BuildRequires:  automake
BuildRequires:  libtool
Requires:       tcl(abi) = %{tcl_version}
Provides:       %{pkgname} = %{version}-%{release}
Provides:       %{pkgname}%{?_isa} = %{version}-%{release}

%description
The tclreadline package makes the GNU Readline library available
for interactive tcl shells. This includes history expansion and
file/command completion. Command completion for all tcl/tk commands
is provided and command completion for user defined commands can
be easily added. Tclreadline can also be used for tcl scripts which
want to use a shell like input interface.

%package devel
Summary:        Development files for the tclreadline library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The tclreadline-devel package includes the header file and library
necessary for developing programs which use the tclreadline library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}
libtoolize
autoreconf%{?el8:27}%{?el9:27}

%build
%configure --libdir=%{tcl_sitearch}/%{pkgname}%{version} --with-tcl=%{_libdir} --with-tk=no

%make_build

%install
%make_install

# Move the library for linking back to %%{_libdir}
mv -f $RPM_BUILD_ROOT{%{tcl_sitearch}/%{pkgname}%{version},%{_libdir}}/lib%{pkgname}-%{version}.so
rm -f $RPM_BUILD_ROOT%{tcl_sitearch}/%{pkgname}%{version}/lib%{pkgname}.so
ln -s ../../lib%{pkgname}-%{version}.so $RPM_BUILD_ROOT%{tcl_sitearch}/%{pkgname}%{version}/lib%{pkgname}.so
ln -s lib%{pkgname}-%{version}.so $RPM_BUILD_ROOT%{_libdir}/lib%{pkgname}.so

%check
cp -prf $RPM_BUILD_ROOT%{_libdir} test
sed -e "s|%{tcl_sitearch}|$(pwd)/test/tcl%{tcl_version}|" \
    -i test/tcl%{tcl_version}/%{pkgname}%{version}/tclreadlineInit.tcl
echo "package require tclreadline" > load.tcl
TCLLIBPATH="$(pwd)/test/tcl%{tcl_version}" tclsh load.tcl

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README.md sample.tclshrc
%{_libdir}/lib%{pkgname}-%{version}.so
%{tcl_sitearch}/%{pkgname}%{version}
%{_mandir}/mann/%{pkgname}.n*

%files devel
%{_libdir}/lib%{pkgname}.so
%{_includedir}/%{pkgname}.h

%changelog
%autochangelog
