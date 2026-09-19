%global source0_hash c8c83d5ece5768e58ca277b2e38af340503c0e53a1a5408c138b33605b7dc8cb

Summary:	C++ interface for Clutter
Name:		cluttermm
Version:	1.17.3
Release:	29%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.gtkmm.org/
Source0:	http://download.gnome.org/sources/cluttermm/1.17/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:	atkmm-devel
BuildRequires:	clutter-devel
BuildRequires:	gtkmm30-devel
BuildRequires:	pangomm-devel
BuildRequires: make

%description
Cluttermm is a C++ interface for Clutter: a software library for creating
fast, visually rich graphical user interfaces.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package	doc
Summary:	API documentation for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-silent-rules

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc COPYING NEWS
%{_libdir}/libcluttermm-1.0.so.*

%files devel
%doc examples/actor.png
%doc examples/test-actors.cc
%doc examples/test-boxes.cc
%{_libdir}/libcluttermm-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/%{name}-1.0
%{_datadir}/%{name}-1.0
%{_includedir}/%{name}-1.0

%files doc
%doc %{_docdir}/cluttermm-1.0/
%doc %{_datadir}/devhelp/

%changelog
%autochangelog
